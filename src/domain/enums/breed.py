from dataclasses import dataclass

from src.domain.animal.cat.enum import CatBreeds


@dataclass(frozen=True)
class Breeds:
    cat = CatBreeds
