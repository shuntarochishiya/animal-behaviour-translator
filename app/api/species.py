from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.species import Species
from app.schemas.species import SpeciesResponse


router = APIRouter(
    prefix="/species",
    tags=["species"],
)


@router.get("", response_model=list[SpeciesResponse])
def get_species(
    db: Session = Depends(get_db),
) -> list[Species]:
    statement = select(Species).order_by(Species.id)

    return list(
        db.scalars(statement).all()
    )


@router.get("/{slug}", response_model=SpeciesResponse)
def get_species_by_slug(
    slug: str,
    db: Session = Depends(get_db),
) -> Species:
    statement = select(Species).where(
        Species.slug == slug
    )

    species = db.scalar(statement)

    if species is None:
        raise HTTPException(
            status_code=404,
            detail="Species not found",
        )

    return species
