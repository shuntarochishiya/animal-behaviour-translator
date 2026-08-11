from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.interpretation_rules import InterpretationRule
from app.models.signals import Signal
from app.models.species import Species
from app.schemas.observation_options import (
    ObservationOptionsResponse,
    SignalOption,
)


router = APIRouter(
    prefix="/observation-options",
    tags=["observation"],
)


@router.get(
    "/{species_slug}",
    response_model=ObservationOptionsResponse,
)
def get_observation_options(
    species_slug: str,
    db: Session = Depends(get_db),
) -> ObservationOptionsResponse:
    species = db.scalar(
        select(Species).where(
            Species.slug == species_slug
        )
    )

    if species is None:
        raise HTTPException(
            status_code=404,
            detail="Species not found",
        )

    signals = db.scalars(
        select(Signal)
        .where(
            Signal.species_id == species.id
        )
        .order_by(
            Signal.category,
            Signal.name,
        )
    ).all()

    context_rows = db.scalars(
        select(
            InterpretationRule.context_slug
        )
        .where(
            InterpretationRule.species_id == species.id
        )
        .distinct()
        .order_by(
            InterpretationRule.context_slug
        )
    ).all()

    return ObservationOptionsResponse(
        species=species.slug,
        signals=[
            SignalOption(
                slug=signal.slug,
                name=signal.name,
                category=signal.category,
                description=signal.description,
            )
            for signal in signals
        ],
        contexts=list(context_rows),
    )
