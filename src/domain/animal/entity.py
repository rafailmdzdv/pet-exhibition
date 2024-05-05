from src.domain.common.breed import Breed
from src.domain.common.entity.aggregate_root import AggregateRoot
from src.domain.enums.color import Colors


class Animal(AggregateRoot):
    name: str
    breed: Breed
    age: int
    color: Colors
