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


def _parse_supporting_signals(value: str) -> set[str]:
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
    Calculate an application-generated match score.

    This is NOT a probability reported by scientific research.

    Score:
    - 40 points: primary signal matches
    - 30 points: context matches
    - 20 points: supporting signals
    - 10 points: input completeness

    The final score is capped according to the rule's
    scientific evidence level.
    """

    score = 0

    # Primary signal
    if rule.primary_signal_slug in observed_signals:
        score += 40

    # Context
    if rule.context_slug == context_slug:
        score += 30

    required_supporting = _parse_supporting_signals(
        rule.supporting_signals
    )

    # Supporting signals
    if required_supporting:
        matched_supporting = (
            required_supporting & observed_signals
        )

        support_ratio = (
            len(matched_supporting)
            / len(required_supporting)
        )

        score += round(20 * support_ratio)
    else:
        # No additional behavioural signal required by the rule.
        score += 20

    # Input completeness
    if observed_signals and context_slug:
        score += 10

    evidence_cap = EVIDENCE_SCORE_CAPS.get(
        rule.evidence_level,
        50,
    )

    return min(score, evidence_cap)


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
        .order_by(Source.year.desc())
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
    Match an animal observation against research-backed
    interpretation rules stored in the database.

    The function returns possible interpretations ordered
    by application-generated confidence score.

    Scientific sources remain separate from the algorithmic
    confidence score.
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
        # At minimum, the primary signal must match.
        if rule.primary_signal_slug not in observed_signals:
            continue

        required_supporting = _parse_supporting_signals(
            rule.supporting_signals
        )

        matched_supporting = sorted(
            required_supporting & observed_signals
        )

        missing_supporting = sorted(
            required_supporting - observed_signals
        )

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
                evidence_level=rule.evidence_level,
                evidence_basis=rule.evidence_basis,
                matched_signal=True,
                matched_context=(
                    rule.context_slug == context_slug
                ),
                matched_supporting_signals=(
                    matched_supporting
                ),
                missing_supporting_signals=(
                    missing_supporting
                ),
                limitations=rule.limitations,
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
