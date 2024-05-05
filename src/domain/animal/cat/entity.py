from dataclasses import dataclass
from uuid import uuid4

from src.domain.animal.cat.enum import CatBreeds
from src.domain.animal.entity import Animal
from src.domain.enums.color import Colors


@dataclass(frozen=True)
class Cat(Animal):
    name: str
    breed: CatBreeds
    age: int
    color: Colors

    @classmethod
    def create(cls, name: str, breed: CatBreeds, age: int, color: Colors) -> Animal:  # type: ignore[override]
        return cls(
            id=uuid4(),
            name=name,
            breed=breed,
            age=age,
            color=color,
        )
