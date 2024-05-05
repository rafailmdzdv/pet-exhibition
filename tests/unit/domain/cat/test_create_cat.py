from src.domain.animal.cat.entity import Cat
from src.domain.enums.breed import Breeds
from src.domain.enums.color import Colors


def test_create_cat() -> None:
    cat = Cat.create(
        name="Bob",
        breed=Breeds.cat.SCOTTISH_STRAIGHT,
        age=3,
        color=Colors.BLACK,
    )
    assert cat.name == "Bob"
    assert cat.breed == "Scottish Straight"
    assert cat.color == "black"
