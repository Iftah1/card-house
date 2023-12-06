from dataclasses import dataclass
from entities.card_type import CardType
from entities.card_design_properties import CardDesignProperties


@dataclass
class Card:
    content: str
    type: CardType
    design_properties: CardDesignProperties
