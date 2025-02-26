from pydantic import BaseModel
from .category import Category


class MotdepasseBase(BaseModel):
    name: str
    identifiant: str | None = None
    password: str | None = None
    description: str | None = None
    is_tested: bool = False
    category: list[Category] = []


class Motdepasse(MotdepasseBase):
    id: int