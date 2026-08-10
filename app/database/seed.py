from sqlalchemy import select

from app.database.db import Base, SessionLocal, engine
from app.models.species import Species


SPECIES_DATA = [
    {
        "slug": "dog",
        "common_name": "Domestic dog",
        "scientific_name": "Canis lupus familiaris",
        "description": (
            "Communication may involve vocalizations, "
            "body posture, facial signals and social context."
        ),
    },
    {
        "slug": "cat",
        "common_name": "Domestic cat",
        "scientific_name": "Felis catus",
        "description": (
            "Communication may involve vocalizations, "
            "facial signals, tail and ear positions, "
            "and interaction context."
        ),
    },
    {
        "slug": "horse",
        "common_name": "Domestic horse",
        "scientific_name": "Equus caballus",
        "description": (
            "Communication may involve vocalizations, "
            "ear position, facial expressions, "
            "head posture and social behaviour."
        ),
    },
    {
        "slug": "african-elephant",
        "common_name": "African elephant",
        "scientific_name": "Loxodonta africana",
        "description": (
            "Communication may involve vocalizations, "
            "gestures, touch and social context."
        ),
    },
]


def seed_species() -> None:
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        for data in SPECIES_DATA:
            statement = select(Species).where(
                Species.slug == data["slug"]
            )

            existing_species = db.scalar(statement)

            if existing_species is None:
                db.add(Species(**data))

        db.commit()


if __name__ == "__main__":
    seed_species()
    print("Species seed completed.")
