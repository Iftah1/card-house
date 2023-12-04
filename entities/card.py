from dataclasses import dataclass
from card_type import CardDesignProperties


@dataclass
class Card:
    content: str
    type: CardDesignProperties
