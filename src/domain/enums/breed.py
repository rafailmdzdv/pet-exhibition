from dataclasses import dataclass

from src.domain.cat.enum import CatBreeds


@dataclass(frozen=True)
class Breeds:
    cat = CatBreeds