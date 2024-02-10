from dataclasses import dataclass
from datetime import datetime
from typing import List, Any, Dict

from card_house.infrastructure.entities.card import Card
from card_house.infrastructure.entities.card_type import CardType


@dataclass
class DBCard(Card):
    type: CardType
    content: str
    version: str
    creation_time: datetime
    card_id: str

    @staticmethod
    def cards_list_to_dict(cards: List['DBCard']) -> Dict[str, Any]:
        return {
            "cards": [
                card.to_dict() for card in cards
            ]
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": str(self.type),
            "content": self.content,
            "version": self.version,
            "creation_time": str(self.creation_time),
            "card_id": self.card_id
        }


class CardKeys:
    TYPE = "type"
    CONTENT = "content"
    VERSION = "version"
    CREATION_TIME = "creation_time"
    CARD_ID = "card_id"
    CARDS = "cards"
