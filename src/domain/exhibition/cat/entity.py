import datetime
from dataclasses import dataclass

from src.domain.animal.cat.entity import Cat
from src.domain.exhibition.common.aggregate import Exhibition
from src.domain.exhibition.cat.value_objects.exhibition_id import CatExhibitionId


@dataclass(frozen=True)
class CatExhibition(Exhibition[CatExhibitionId]):
    @classmethod
    def create(cls, cats: list[Cat]) -> Exhibition:
        return cls(
            id=CatExhibitionId.generate(),
            participants=cats,
            date=datetime.datetime.now().date(),
        )
