from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import Dict

from card_type import CardType


@dataclass
class Card:
    content: str
    card_type: CardType
    date: datetime
    version: str
    id: UUID

    def serialize_card(self) -> Dict[str, str]:
        serialized_card = {
            "content": self.content,
            "card_type": self.card_type.value,
            "date": str(self.date),
            "version": self.version,
            "id": self.id
        }
        for key, value in serialized_card.items():
            if value is None:
                serialized_card[key] = "null"

        return serialized_card
