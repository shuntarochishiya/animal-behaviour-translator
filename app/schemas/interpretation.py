from pydantic import BaseModel, Field


class InterpretationRequest(BaseModel):
    species: str = Field(
        examples=["dog"],
    )

    signals: list[str] = Field(
        min_length=1,
        examples=[
            [
                "growl",
                "play-bow",
            ]
        ],
    )

    context: str = Field(
        examples=["play"],
    )


class SourceResponse(BaseModel):
    key: str
    title: str
    authors: str
    year: int
    journal: str | None
    doi: str | None
    url: str


class InterpretationAlternative(BaseModel):
    rule_key: str

    label: str
    description: str

    system_match_score: int

    scientific_evidence: str
    evidence_basis: str

    context_matched: bool

    matched_supporting_signals: list[str]
    missing_supporting_signals: list[str]

    limitations: str

    sources: list[SourceResponse]


class InterpretationResponse(BaseModel):
    status: str

    species: str
    observed_signals: list[str]
    context: str

    primary_interpretation: InterpretationAlternative | None

    alternatives: list[InterpretationAlternative]

    disclaimer: str
