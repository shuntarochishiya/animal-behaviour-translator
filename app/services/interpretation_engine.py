from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.interpretation_rules import InterpretationRule
from app.models.rule_source import RuleSource
from app.models.source import Source
from app.models.species import Species


EVIDENCE_SCORE_CAPS = {
    "strong": 100,
    "moderate": 75,
    "limited": 50,
}


@dataclass
class SourceResult:
    key: str
    title: str
    authors: str
    year: int
    journal: str | None
    doi: str | None
    url: str


@dataclass
class InterpretationResult:
    rule_key: str
    interpretation_label: str
    interpretation_description: str

    confidence_score: int

    evidence_level: str
    evidence_basis: str

    matched_signal: bool
    matched_context: bool

    matched_supporting_signals: list[str]
    missing_supporting_signals: list[str]

    limitations: str

    sources: list[SourceResult]


def _parse_supporting_signals(
    value: str,
) -> set[str]:

    if not value:
        return set()

    if not value.strip():
        return set()

    return {
        signal.strip()
        for signal in value.split(",")
        if signal.strip()
    }


def _calculate_confidence(
    rule: InterpretationRule,
    observed_signals: set[str],
    context_slug: str,
) -> int:
    """
    Application-generated matching score.

    This is NOT a scientific probability.

    Score:
    - 40 points: primary signal match
    - 30 points: context match
    - 20 points: supporting signal match
    - 10 points: complete input
    """

    score = 0


    # Primary signal
    if rule.primary_signal_slug in observed_signals:
        score += 40


    # Context
    if rule.context_slug == context_slug:
        score += 30


    # Supporting signals
    required_supporting = _parse_supporting_signals(
        rule.supporting_signals
    )

    if required_supporting:

        matched_supporting = (
            required_supporting & observed_signals
        )

        support_ratio = (
            len(matched_supporting)
            /
            len(required_supporting)
        )

        score += round(
            20 * support_ratio
        )

    else:
        score += 20


    # Input completeness
    if observed_signals and context_slug:
        score += 10


    evidence_cap = EVIDENCE_SCORE_CAPS.get(
        rule.evidence_level,
        50,
    )


    return min(
        score,
        evidence_cap,
    )


def _get_rule_sources(
    db: Session,
    rule_id: int,
) -> list[SourceResult]:

    statement = (
        select(Source)
        .join(
            RuleSource,
            RuleSource.source_id == Source.id,
        )
        .where(
            RuleSource.rule_id == rule_id
        )
        .order_by(
            Source.year.desc()
        )
    )


    sources = db.scalars(statement).all()


    return [
        SourceResult(
            key=source.key,
            title=source.title,
            authors=source.authors,
            year=source.year,
            journal=source.journal,
            doi=source.doi,
            url=source.url,
        )
        for source in sources
    ]


def interpret_observation(
    db: Session,
    species_slug: str,
    signals: list[str],
    context_slug: str,
) -> list[InterpretationResult]:
    """
    Match observations against research-backed rules.

    Rules are matched using:
    - primary signals
    - supporting signals
    - context
    """


    species = db.scalar(
        select(Species).where(
            Species.slug == species_slug
        )
    )


    if species is None:
        raise ValueError(
            f"Unknown species: {species_slug}"
        )


    observed_signals = {
        signal.strip()
        for signal in signals
        if signal.strip()
    }


    if not observed_signals:
        return []


    rules = db.scalars(
        select(InterpretationRule).where(
            InterpretationRule.species_id == species.id
        )
    ).all()


    results: list[InterpretationResult] = []


    for rule in rules:

        matched_primary = (
            rule.primary_signal_slug
            in observed_signals
        )


        required_supporting = _parse_supporting_signals(
            rule.supporting_signals
        )


        matched_supporting = sorted(
            required_supporting & observed_signals
        )


        missing_supporting = sorted(
            required_supporting - observed_signals
        )


        # New logic:
        # at least one signal must match
        if (
            not matched_primary
            and not matched_supporting
        ):
            continue


        confidence = _calculate_confidence(
            rule=rule,
            observed_signals=observed_signals,
            context_slug=context_slug,
        )


        results.append(
            InterpretationResult(
                rule_key=rule.key,

                interpretation_label=(
                    rule.interpretation_label
                ),

                interpretation_description=(
                    rule.interpretation_description
                ),


                confidence_score=confidence,


                evidence_level=(
                    rule.evidence_level
                ),

                evidence_basis=(
                    rule.evidence_basis
                ),


                matched_signal=(
                    matched_primary
                ),


                matched_context=(
                    rule.context_slug
                    == context_slug
                ),


                matched_supporting_signals=(
                    matched_supporting
                ),


                missing_supporting_signals=(
                    missing_supporting
                ),


                limitations=(
                    rule.limitations
                ),


                sources=_get_rule_sources(
                    db=db,
                    rule_id=rule.id,
                ),
            )
        )


    results.sort(
        key=lambda result: result.confidence_score,
        reverse=True,
    )


    return results


def aggregate_evidence(
    results: list[InterpretationResult],
) -> dict:

    evidence_basis = []
    limitations = []
    sources = {}


    for result in results:

        if result.evidence_basis:
            evidence_basis.append(
                result.evidence_basis
            )


        if result.limitations:
            limitations.append(
                result.limitations
            )


        for source in result.sources:
            sources[source.key] = source


    return {
        "evidence_basis": list(
            dict.fromkeys(
                evidence_basis
            )
        ),

        "limitations": list(
            dict.fromkeys(
                limitations
            )
        ),

        "sources": list(
            sources.values()
        ),
    }
