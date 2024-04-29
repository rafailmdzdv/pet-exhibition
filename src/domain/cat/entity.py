from dataclasses import dataclass
from typing import Self
from uuid import uuid4

from src.domain.cat.enum import CatBreeds
from src.domain.common.entity.aggregate_root import AggregateRoot
from src.domain.enums.color import Colors


@dataclass(frozen=True)
class Cat(AggregateRoot):
    name: str
    breed: CatBreeds
    age: int
    color: Colors

    @classmethod
    def create(cls, name: str, breed: CatBreeds, age: int, color: Colors) -> Self:  # type: ignore[override]
        return cls(
            id=uuid4(),
            name=name,
            breed=breed,
            age=age,
            color=color,
        )
