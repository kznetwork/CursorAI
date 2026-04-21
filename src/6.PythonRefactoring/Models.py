from dataclasses import dataclass
from decimal import Decimal

@dataclass
class User:
    id: int
    name: str


@dataclass
class Menu:
    id: int
    name: str
    price: Decimal