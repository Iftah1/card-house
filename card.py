from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from card_kind import Kind


@dataclass
class Card:
    content: str
    kind: Kind
    date: datetime
    version: str
    id: UUID
