import datetime

from src.domain.cat.entity import Cat
from src.domain.exhibition.cat.entity import CatExhibition


def test_create_cat_exhibition(cats: list[Cat]) -> None:
    exhibition = CatExhibition.create(
        cats=cats,
    )
    assert exhibition.date == datetime.datetime.now().date()
    assert exhibition.participants[0].name == "Bob"  # type: ignore
