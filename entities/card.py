from dataclasses import dataclass
from entities.card_type import CardType
from entities.card_design_properties import CardDesignProperties
from datetime import datetime
from uuid import UUID
from typing import Dict
from card_type import CardType



@dataclass
class Card:
    content: str
    type: CardType
    design_properties: CardDesignProperties
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
