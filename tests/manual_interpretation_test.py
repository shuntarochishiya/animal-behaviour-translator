from app.database.db import SessionLocal
from app.services.interpretation_engine import (
    interpret_observation,
)


def main() -> None:
    with SessionLocal() as db:
        results = interpret_observation(
            db=db,
            species_slug="dog",
            signals=[
                "growl",
                "play-bow",
            ],
            context_slug="play",
        )

        for result in results:
            print()
            print("=" * 70)

            print(
                f"Interpretation: "
                f"{result.interpretation_label}"
            )

            print(
                f"System confidence: "
                f"{result.confidence_score}/100"
            )

            print(
                f"Evidence: "
                f"{result.evidence_level}"
            )

            print(
                f"Context matched: "
                f"{result.matched_context}"
            )

            print(
                "Matched supporting signals:",
                result.matched_supporting_signals,
            )

            print(
                "Missing supporting signals:",
                result.missing_supporting_signals,
            )

            print()
            print("Sources:")

            for source in result.sources:
                print(
                    f"- {source.authors} "
                    f"({source.year}) "
                    f"{source.title}"
                )

                print(
                    f"  {source.url}"
                )

            print()
            print(
                "Limitations:",
                result.limitations,
            )


if __name__ == "__main__":
    main()
