import datetime
from dataclasses import dataclass

from src.domain.common.entity.aggregate_root import AggregateRoot


@dataclass(frozen=True)
class Exhibition(AggregateRoot):
    date: datetime.date
