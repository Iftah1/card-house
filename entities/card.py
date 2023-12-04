from dataclasses import dataclass
from entities.card_type import CardDesignProperties


@dataclass
class Card:
    content: str
    type: CardDesignProperties
