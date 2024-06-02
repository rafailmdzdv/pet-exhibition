from typing import Generic, TypeVar
from uuid import UUID

from src.domain.common.entity import Entity
from src.domain.common.value_object import ValueObject

T = TypeVar("T", bound=ValueObject[UUID])


class Animal(Entity[T], Generic[T]):
    name: str
    age: int
