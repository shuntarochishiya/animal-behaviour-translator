from sqlalchemy import select

from app.database.db import Base, SessionLocal, engine
from app.models.species import Species
from app.models.signals import Signal
from app.models.source import Source

from app.models.interpretation_rules import InterpretationRule
from app.models.rule_source import RuleSource


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
]


DOG_SIGNALS = [
    {
        "slug": "bark",
        "name": "Bark",
        "category": "vocalization",
        "description": (
            "A common canine vocalization whose acoustic "
            "properties may vary across behavioural contexts."
        ),
    },
    {
        "slug": "growl",
        "name": "Growl",
        "category": "vocalization",
        "description": (
            "A low-frequency vocalization that may occur "
            "in several contexts including play and conflict."
        ),
    },
    {
        "slug": "whine",
        "name": "Whine",
        "category": "vocalization",
        "description": (
            "A tonal vocalization that may occur in contact, "
            "separation or elevated-arousal situations."
        ),
    },
    {
        "slug": "howl",
        "name": "Howl",
        "category": "vocalization",
        "description": (
            "A prolonged vocalization involved in canine "
            "social and long-distance communication."
        ),
    },
    {
        "slug": "play-bow",
        "name": "Play bow",
        "category": "posture",
        "description": (
            "A posture with lowered forequarters and raised "
            "hindquarters commonly associated with play interaction."
        ),
    },
    {
        "slug": "stiff-body",
        "name": "Stiff body",
        "category": "posture",
        "description": (
            "Visible increase in overall body rigidity or tension."
        ),
    },
    {
        "slug": "lowered-body",
        "name": "Lowered body",
        "category": "posture",
        "description": (
            "A lowered body posture that may occur in fearful "
            "or defensive contexts."
        ),
    },
    {
        "slug": "tail-tucked",
        "name": "Tucked tail",
        "category": "posture",
        "description": (
            "Tail positioned low or tucked beneath the body."
        ),
    },
    {
        "slug": "ears-back",
        "name": "Ears back",
        "category": "facial",
        "description": (
            "Ears held or drawn backward relative to their "
            "neutral position."
        ),
    },
    {
        "slug": "tail-wagging",
        "name": "Tail wagging",
        "category": "movement",
        "description": (
            "Repeated lateral movement of the tail. Tail wagging is "
            "a socially relevant signal, but its meaning depends on "
            "context, tail position, movement characteristics and "
            "other accompanying behaviours."
        ),
    }
]


DOG_SOURCES = [
    {
        "key": "siniscalchi_2018",
        "title": "Communication in Dogs",
        "authors": "Siniscalchi M., d'Ingeo S., Minunno M., Quaranta A.",
        "year": 2018,
        "journal": "Animals",
        "doi": "10.3390/ani8080131",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6116041/",
        "source_type": "review",
        "evidence_notes": (
            "Review of visual, acoustic, olfactory and tactile "
            "communication in domestic dogs."
        ),
    },
    {
        "key": "farago_2017",
        "title": (
            "Dog growls express various contextual and affective "
            "content for human listeners"
        ),
        "authors": (
            "Faragó T., Takács N., Miklósi Á., Pongrácz P."
        ),
        "year": 2017,
        "journal": "Royal Society Open Science",
        "doi": "10.1098/rsos.170134",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5451822/",
        "source_type": "experimental",
        "evidence_notes": (
            "Experimental study of dog growls recorded in different "
            "social contexts. Human listeners identified some contexts "
            "above chance."
        ),
    },
    {
        "key": "byosiere_2016",
        "title": (
            "Investigating the Function of Play Bows in Dog and "
            "Wolf Puppies"
        ),
        "authors": (
            "Byosiere S. E., Espinosa J., Marshall-Pescini S., "
            "Smuts B."
        ),
        "year": 2016,
        "journal": "PLoS ONE",
        "doi": None,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5199004/",
        "source_type": "observational",
        "evidence_notes": (
            "Play bows in young dogs frequently occurred around brief "
            "pauses followed by highly active play."
        ),
    },
    {
        "key": "maglieri_2022",
        "title": (
            "Don't stop me now, I'm having such a good time: "
            "Domestic dogs use play bows to maintain social play"
        ),
        "authors": "Maglieri V. et al.",
        "year": 2022,
        "journal": "Current Zoology",
        "doi": None,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10039175/",
        "source_type": "observational",
        "evidence_notes": (
            "Play bows were associated with restoring or maintaining "
            "the partner's motivation to continue social play."
        ),
    },
    {
        "key": "marx_2021",
        "title": (
            "Occurrences of non-linear phenomena and vocal harshness "
            "in dog whines as indicators of stress and arousal"
        ),
        "authors": "Marx A. et al.",
        "year": 2021,
        "journal": "Scientific Reports",
        "doi": None,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7904949/",
        "source_type": "experimental",
        "evidence_notes": (
            "Study of thousands of whines recorded during separation "
            "situations, relating acoustic characteristics to behavioural "
            "arousal and separation-related responses."
        ),
    },
    {
        "key": "capitain_2025",
        "title": (
            "Differences in dogs' and wolves' human-directed "
            "greeting behaviour towards bonded and familiar humans"
        ),
        "authors": "Capitain S. et al.",
        "year": 2025,
        "journal": None,
        "doi": None,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12226620/",
        "source_type": "observational",
        "evidence_notes": (
            "Study of human-directed greeting behaviour in dogs and wolves. "
            "Dogs showed more proximity, gazing and tail wagging towards humans, "
            "and frequently displayed rotated or downward ear positions."
        ),
    },
    {
        "key": "leonetti_2024",
        "title": "Why do dogs wag their tails?",
        "authors": "Leonetti S. et al.",
        "year": 2024,
        "journal": None,
        "doi": None,
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10792393/",
        "source_type": "review",
        "evidence_notes": (
            "Review of dog tail wagging and its communicative significance. "
            "The interpretation of wagging depends on multiple features, "
            "including tail carriage, movement characteristics and lateralization. "
            "Tail wagging should not be treated as a universal indicator "
            "of positive emotion."
        ),
    },
]

DOG_RULES = [
    {
        "key": "dog_play_bow_play",
        "primary_signal_slug": "play-bow",
        "context_slug": "play",
        "supporting_signals": "",
        "interpretation_label": "Play solicitation or continuation",
        "interpretation_description": (
            "A play bow observed during a social play interaction is "
            "consistent with initiating, resuming, or maintaining play."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Play bows have been directly studied in dog social play. "
            "Observational research found that they frequently occur around "
            "brief interruptions in play and may help initiate or maintain "
            "continued playful interaction."
        ),
        "limitations": (
            "The posture should be interpreted within a social play context. "
            "It should not be treated as a literal linguistic message or as "
            "proof of a specific internal emotional state."
        ),
        "source_keys": [
            "byosiere_2016",
            "maglieri_2022",
        ],
    },

    {
        "key": "dog_growl_play",
        "primary_signal_slug": "growl",
        "context_slug": "play",
        "supporting_signals": "play-bow",
        "interpretation_label": "Play-related vocalization",
        "interpretation_description": (
            "Growling that occurs during an ongoing play interaction, "
            "especially when accompanied by recognizable play behaviour, "
            "is consistent with a playful context and should not automatically "
            "be interpreted as aggression."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Experimental work has compared dog growls recorded in different "
            "contexts, including play, food guarding, and threatening situations. "
            "The study found that growls can carry context-dependent and "
            "affective information."
        ),
        "limitations": (
            "Growling occurs in several different motivational contexts. "
            "A growl without contextual information is insufficient for a "
            "reliable interpretation."
        ),
        "source_keys": [
            "farago_2017",
            "siniscalchi_2018",
        ],
    },

    {
        "key": "dog_growl_resource",
        "primary_signal_slug": "growl",
        "context_slug": "resource",
        "supporting_signals": "stiff-body",
        "interpretation_label": "Competitive or warning-related context",
        "interpretation_description": (
            "Growling in a resource-related interaction is consistent with "
            "competitive or warning-related communication."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Food-guarding growls were one of the experimentally studied "
            "contexts in Faragó et al. The results support the conclusion "
            "that growls can contain information related to the social "
            "context in which they are produced."
        ),
        "limitations": (
            "The presence of a growl does not establish that an attack will "
            "occur. The signal should be interpreted together with the "
            "interaction context and other behavioural observations."
        ),
        "source_keys": [
            "farago_2017",
            "siniscalchi_2018",
        ],
    },

    {
        "key": "dog_whine_separation",
        "primary_signal_slug": "whine",
        "context_slug": "separation",
        "supporting_signals": "",
        "interpretation_label": "Separation-related arousal or contact seeking",
        "interpretation_description": (
            "Whining observed during separation is consistent with "
            "separation-related arousal or contact-seeking behaviour."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Research on dog whines recorded during separation found "
            "associations between acoustic properties of whining and "
            "behavioural arousal. However, the presence of a whine alone "
            "does not uniquely identify distress."
        ),
        "limitations": (
            "Whining can occur in many situations. Without additional "
            "behavioural or acoustic information, the system should not "
            "interpret the signal as proof of distress or anxiety."
        ),
        "source_keys": [
            "marx_2021",
        ],
    },
    {
        "key": "dog_tail_wag_greeting",
        "primary_signal_slug": "tail-wagging",
        "context_slug": "greeting",
        "supporting_signals": "ears-back",
        "interpretation_label": "Affiliative greeting-related response",
        "interpretation_description": (
            "Tail wagging during greeting, especially when accompanied "
            "by socially directed body signals such as ears held back, "
            "is consistent with an affiliative human-directed greeting response."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Research on dog-human greeting behaviour reports tail wagging "
            "together with proximity and gaze towards humans. Dogs may also "
            "display rotated or downward ear positions during these interactions. "
            "However, tail wagging alone is not specific to positive emotion."
        ),
        "limitations": (
            "Tail wagging should not be interpreted as a direct measure of "
            "happiness. Tail position, movement characteristics, individual "
            "variation and the broader social context should also be considered."
        ),
        "source_keys": [
            "capitain_2025",
            "siniscalchi_2018",
            "leonetti_2024",
        ],
    },
]

def seed_database() -> None:
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        for data in SPECIES_DATA:
            existing = db.scalar(
                select(Species).where(
                    Species.slug == data["slug"]
                )
            )

            if existing is None:
                db.add(Species(**data))

        db.commit()

        dog = db.scalar(
            select(Species).where(
                Species.slug == "dog"
            )
        )

        if dog is None:
            raise RuntimeError("Dog species was not created.")

        for data in DOG_SIGNALS:
            existing = db.scalar(
                select(Signal).where(
                    Signal.species_id == dog.id,
                    Signal.slug == data["slug"],
                )
            )

            if existing is None:
                db.add(
                    Signal(
                        species_id=dog.id,
                        **data,
                    )
                )

        for data in DOG_SOURCES:
            existing = db.scalar(
                select(Source).where(
                    Source.key == data["key"]
                )
            )

            if existing is None:
                db.add(Source(**data))

        dog = db.scalar(
            select(Species).where(
                Species.slug == "dog"
            )
        )

        if dog is None:
            raise RuntimeError("Dog species not found.")

        for rule_data in DOG_RULES:
            source_keys = rule_data["source_keys"]

            existing_rule = db.scalar(
                select(InterpretationRule).where(
                    InterpretationRule.key == rule_data["key"]
                )
            )

            if existing_rule is None:
                rule = InterpretationRule(
                    species_id=dog.id,
                    key=rule_data["key"],
                    primary_signal_slug=rule_data["primary_signal_slug"],
                    context_slug=rule_data["context_slug"],
                    supporting_signals=rule_data["supporting_signals"],
                    interpretation_label=rule_data["interpretation_label"],
                    interpretation_description=(
                        rule_data["interpretation_description"]
                    ),
                    evidence_level=rule_data["evidence_level"],
                    evidence_basis=rule_data["evidence_basis"],
                    limitations=rule_data["limitations"],
                )

                db.add(rule)
                db.flush()

                for source_key in source_keys:
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

        db.commit()


if __name__ == "__main__":
    seed_database()
    print("Database seed completed.")


if __name__ == "__main__":
    seed_database()
    print("Species seed completed.")
