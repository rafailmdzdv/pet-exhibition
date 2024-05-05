import pytest

from src.domain.animal.entity import Animal
from src.domain.animal.cat.entity import Cat
from src.domain.enums.breed import Breeds
from src.domain.enums.color import Colors


@pytest.fixture(name="cats")
def create_cats() -> list[Animal]:
    names = ["Bob", "Gustav", "Patriciy", "Mr. Fresh"]
    return [
        Cat.create(name, Breeds.cat.SCOTTISH_STRAIGHT, 3, Colors.BLACK)
        for name in names
    ]
