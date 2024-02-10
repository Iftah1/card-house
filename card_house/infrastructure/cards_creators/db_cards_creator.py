from datetime import datetime
from typing import List
from uuid import uuid4

from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.entities.card import Card
from card_house.infrastructure.entities.db_card import DBCard


class DBCardsCreator(ICardsCreator):
    def create_card(self, card: Card) -> DBCard:
        return DBCard(
            content=card.content,
            type=card.type,
            version="v1",
            creation_time=datetime.now(),
            card_id=str(uuid4())
        )

    def create_cards(self, cards: List[Card]) -> List[DBCard]:
        resulted_cards = []
        for card in cards:
            resulted_cards.append(self.create_card(card))
        return resulted_cards
