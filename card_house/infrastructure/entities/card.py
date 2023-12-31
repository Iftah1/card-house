from dataclasses import dataclass
from card_house.infrastructure.entities.card_type import CardType


@dataclass
class Card:
    content: str
    type: CardType
