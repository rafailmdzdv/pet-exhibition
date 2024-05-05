import datetime
from dataclasses import dataclass
from typing import Sequence

from src.domain.common.entity.aggregate_root import AggregateRoot


@dataclass(frozen=True)
class Exhibition(AggregateRoot):
    participants: Sequence[AggregateRoot]
    date: datetime.date
