from typing import Any, Generic, Protocol, TypeVar

T = TypeVar("T")


class ValueObject(Protocol, Generic[T]):
    value: T

    def to_raw(self) -> Any: ...
