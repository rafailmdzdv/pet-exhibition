import datetime
from dataclasses import dataclass
from typing import Self
from uuid import uuid4

from src.domain.cat.entity import Cat
from src.domain.common.entity.aggregate_root import AggregateRoot


@dataclass(frozen=True)
class CatExhibition(AggregateRoot):
    cats: list[Cat]
    date: datetime.datetime

    @classmethod
    def create(cls, cats: list[Cat], date: datetime.datetime) -> Self:  # type: ignore[override]
        return cls(
            id=uuid4(),
            cats=cats,
            date=date,
        )
