from pydantic import BaseModel, ConfigDict


class SpeciesResponse(BaseModel):
    id: int
    slug: str
    common_name: str
    scientific_name: str
    description: str

    model_config = ConfigDict(from_attributes=True)
