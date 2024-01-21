from dataclasses import dataclass
from typing import List, Dict, Any

from card_house.infrastructure.entities.card import Card

Row = List["PrintedCard"]
Page = List[Row]


@dataclass
class PrintedCard(Card):
    title: str
    sign: str
    design_id: str
