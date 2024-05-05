import datetime
from dataclasses import dataclass
from uuid import uuid4

from src.domain.cat.entity import Cat
from src.domain.exhibition.entity import Exhibition


@dataclass(frozen=True)
class CatExhibition(Exhibition):
    cats: list[Cat]

    @classmethod
    def create(cls, cats: list[Cat]) -> Exhibition:  # type: ignore[override]
        return cls(
            id=uuid4(),
            cats=cats,
            date=datetime.datetime.now().date(),
        )
