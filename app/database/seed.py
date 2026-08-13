from types import ModuleType

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.database.db import Base, SessionLocal, engine
from app.database.seed_data import cat, dog, elephant, horse, duck

from app.models.interpretation_rules import InterpretationRule
from app.models.rule_source import RuleSource
from app.models.signals import Signal
from app.models.source import Source
from app.models.species import Species


SPECIES_DATA = [
    {
        "slug": "dog",
        "common_name": "Domestic dog",
        "scientific_name": "Canis lupus familiaris",
        "description": (
            "Communication may involve vocalizations, body posture, "
            "facial signals and social context."
        ),
    },
    {
        "slug": "cat",
        "common_name": "Domestic cat",
        "scientific_name": "Felis catus",
        "description": (
            "Communication may involve vocalizations, facial signals, "
            "tail and ear positions, and interaction context."
        ),
    },
    {
        "slug": "horse",
        "common_name": "Domestic horse",
        "scientific_name": "Equus caballus",
        "description": (
            "Communication may involve vocalizations, ear position, "
            "facial expressions, head posture and social behaviour."
        ),
    },
    {
        "slug": "african-elephant",
        "common_name": "African elephant",
        "scientific_name": "Loxodonta africana",
        "description": (
            "Communication may involve vocalizations, gestures, "
            "touch and social context."
        ),
    },
    {
        "slug": "duck",
        "common_name": "Domestic duck",
        "scientific_name": "Anas platyrhynchos domesticus",
        "description": (
            "Communication may involve vocalizations, "
            "courtship displays, body movements, "
            "and social interactions."
        ),
    },
]


ANIMALS = [
    ("dog", dog),
    ("cat", cat),
    ("horse", horse),
    ("african-elephant", elephant),
    ("duck", duck)
]


def seed_species(
    db: Session,
) -> None:
    for data in SPECIES_DATA:
        species = db.scalar(
            select(Species).where(
                Species.slug == data["slug"]
            )
        )

        if species is None:
            species = Species(**data)
            db.add(species)
            continue

        species.common_name = data["common_name"]
        species.scientific_name = data["scientific_name"]
        species.description = data["description"]


def seed_signals(
    db: Session,
    species: Species,
    animal_module: ModuleType,
) -> None:

    for data in animal_module.SIGNALS:
        signal = db.scalar(
            select(Signal).where(
                Signal.species_id == species.id,
                Signal.slug == data["slug"],
            )
        )

        if signal is None:
            db.add(
                Signal(
                    species_id=species.id,
                    **data,
                )
            )
            continue

        signal.name = data["name"]
        signal.category = data["category"]
        signal.description = data["description"]


def seed_sources(
    db: Session,
    animal_module: ModuleType,
) -> None:

    for data in animal_module.SOURCES:
        source = db.scalar(
            select(Source).where(
                Source.key == data["key"]
            )
        )

        if source is None:
            db.add(Source(**data))
            continue

        source.title = data["title"]
        source.authors = data["authors"]
        source.year = data["year"]
        source.journal = data["journal"]
        source.doi = data["doi"]
        source.url = data["url"]
        source.source_type = data["source_type"]
        source.evidence_notes = data["evidence_notes"]


def seed_rules(
    db: Session,
    species: Species,
    animal_module: ModuleType,
) -> None:

    for rule_data in animal_module.RULES:

        rule = db.scalar(
            select(InterpretationRule).where(
                InterpretationRule.key == rule_data["key"]
            )
        )

        if rule is None:
            rule = InterpretationRule(
                species_id=species.id,
                key=rule_data["key"],
                primary_signal_slug=(
                    rule_data["primary_signal_slug"]
                ),
                context_slug=rule_data["context_slug"],
                supporting_signals=(
                    rule_data["supporting_signals"]
                ),
                interpretation_label=(
                    rule_data["interpretation_label"]
                ),
                interpretation_description=(
                    rule_data["interpretation_description"]
                ),
                evidence_level=(
                    rule_data["evidence_level"]
                ),
                evidence_basis=(
                    rule_data["evidence_basis"]
                ),
                limitations=(
                    rule_data["limitations"]
                ),
            )

            db.add(rule)
            db.flush()

        else:
            rule.species_id = species.id

            rule.primary_signal_slug = (
                rule_data["primary_signal_slug"]
            )

            rule.context_slug = (
                rule_data["context_slug"]
            )

            rule.supporting_signals = (
                rule_data["supporting_signals"]
            )

            rule.interpretation_label = (
                rule_data["interpretation_label"]
            )

            rule.interpretation_description = (
                rule_data["interpretation_description"]
            )

            rule.evidence_level = (
                rule_data["evidence_level"]
            )

            rule.evidence_basis = (
                rule_data["evidence_basis"]
            )

            rule.limitations = (
                rule_data["limitations"]
            )


        db.flush()


        db.execute(
            delete(RuleSource).where(
                RuleSource.rule_id == rule.id
            )
        )


        for source_key in rule_data["source_keys"]:

            source = db.scalar(
                select(Source).where(
                    Source.key == source_key
                )
            )

            if source is None:
                raise RuntimeError(
                    f"Source not found: {source_key}"
                )


            db.add(
                RuleSource(
                    rule_id=rule.id,
                    source_id=source.id,
                )
            )


def seed_animal(
    db: Session,
    species_slug: str,
    animal_module: ModuleType,
) -> None:

    species = db.scalar(
        select(Species).where(
            Species.slug == species_slug
        )
    )

    if species is None:
        raise RuntimeError(
            f"Species not found: {species_slug}"
        )


    seed_signals(
        db=db,
        species=species,
        animal_module=animal_module,
    )


    seed_sources(
        db=db,
        animal_module=animal_module,
    )


    db.flush()


    seed_rules(
        db=db,
        species=species,
        animal_module=animal_module,
    )


def seed_database() -> None:

    Base.metadata.create_all(bind=engine)


    with SessionLocal() as db:

        seed_species(db)

        db.flush()


        for species_slug, animal_module in ANIMALS:

            seed_animal(
                db=db,
                species_slug=species_slug,
                animal_module=animal_module,
            )


        db.commit()


if __name__ == "__main__":
    seed_database()
    print("Database seed completed.")
