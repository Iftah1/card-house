from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from entities.card_type import CardType


@dataclass
class CardProperties:
    content: str
    version: str
    type: CardType
    date: datetime
    id: UUID
