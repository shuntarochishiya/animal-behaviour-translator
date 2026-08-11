from pydantic import BaseModel


class SignalOption(BaseModel):
    slug: str
    name: str
    category: str
    description: str


class ObservationOptionsResponse(BaseModel):
    species: str
    signals: list[SignalOption]
    contexts: list[str]
