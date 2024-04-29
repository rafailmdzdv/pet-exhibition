from abc import ABC, abstractmethod
from typing import Self

from src.domain.common.entity.entity import Entity


class AggregateRoot(Entity, ABC):
    @classmethod
    @abstractmethod
    def create(cls, **kwargs) -> Self: ...
