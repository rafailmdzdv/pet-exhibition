import datetime

from src.domain.cat.entity import Cat
from src.domain.exhibition.cat.entity import CatExhibition


def test_create_cat_exhibition(cats: list[Cat]) -> None:
    exhibition = CatExhibition.create(
        cats=cats,
        date=datetime.datetime(2024, 4, 30, 15),
    )
    assert exhibition.date == datetime.datetime(2024, 4, 30, 15)
    assert exhibition.cats[0].name == "Bob"
