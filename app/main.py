from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.interpretation import (
    router as interpretation_router,
)
from app.api.observation_options import (
    router as observation_options_router,
)
from app.api.species import router as species_router


app = FastAPI(
    title="Animal Behaviour Translator API",
    description=(
        "Research-based prototype for interpreting animal "
        "communication and behavioural signals."
    ),
    version="0.2.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(species_router)
app.include_router(interpretation_router)
app.include_router(observation_options_router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "Animal Behaviour Translator API",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
    }
