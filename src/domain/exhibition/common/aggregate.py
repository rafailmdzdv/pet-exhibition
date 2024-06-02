import datetime
from dataclasses import dataclass
from typing import Generic, Sequence, TypeVar

from src.domain.animal.common.aggregate import Animal
from src.domain.common.entity import Entity
from src.domain.common.value_object import ValueObject

T = TypeVar("T", bound=ValueObject)


@dataclass(frozen=True)
class Exhibition(Entity[T], Generic[T]):
    participants: Sequence[Animal]
    date: datetime.date
