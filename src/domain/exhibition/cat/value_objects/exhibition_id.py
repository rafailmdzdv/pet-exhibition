from dataclasses import dataclass
from typing import Any, Self
from uuid import UUID, uuid4

from src.domain.common.value_object import ValueObject


@dataclass(frozen=True)
class CatExhibitionId(ValueObject[UUID]):
    value: UUID

    @classmethod
    def generate(cls) -> Self:
        return cls(uuid4())

    def to_raw(self) -> Any:
        return str(self.value)
