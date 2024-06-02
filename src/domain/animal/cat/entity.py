from dataclasses import dataclass

from src.domain.animal.cat.enum import CatBreeds
from src.domain.animal.cat.value_objects.cat_id import CatId
from src.domain.animal.common.aggregate import Animal
from src.domain.enums.color import Colors


@dataclass(frozen=True)
class Cat(Animal[CatId]):
    name: str
    breed: CatBreeds
    age: int
    color: Colors

    @classmethod
    def create(
        cls, name: str, breed: CatBreeds, age: int, color: Colors
    ) -> Animal[CatId]:
        return cls(
            id=CatId.generate(),
            name=name,
            breed=breed,
            age=age,
            color=color,
        )
