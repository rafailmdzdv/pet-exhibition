import datetime
from dataclasses import dataclass
from typing import Sequence

from src.domain.animal.entity import Animal
from src.domain.common.entity.aggregate_root import AggregateRoot


@dataclass(frozen=True)
class Exhibition(AggregateRoot):
    participants: Sequence[Animal]
    date: datetime.date
