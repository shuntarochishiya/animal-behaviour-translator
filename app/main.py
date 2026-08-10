from fastapi import FastAPI

from app.api.species import router as species_router


app = FastAPI(
    title="Animal Behaviour Translator API",
    description=(
        "Research-based prototype for interpreting animal "
        "communication and behavioural signals."
    ),
    version="0.1.0",
)


app.include_router(species_router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "Animal Behaviour Translator API",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
