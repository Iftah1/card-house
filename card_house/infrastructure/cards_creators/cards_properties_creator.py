from typing import List, Any

from flask import Request

from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.entities.card_type import CardType
from card_house.infrastructure.entities.db_card import DBCard, CardKeys


class CardsPropertiesCreator(ICardsCreator):
    def create_card(self, card: Request) -> DBCard:
        json_card = card.json
        return DBCard(
            card_id=json_card.get(CardKeys.CARD_ID),
            creation_time=json_card.get(CardKeys.CREATION_TIME),
            content=json_card.get(CardKeys.CONTENT),
            version=json_card.get(CardKeys.VERSION),
            type=CardType(json_card.get(CardKeys.TYPE))
        )

    def create_cards(self, cards: Request) -> List[DBCard]:
        resulted_cards = []
        for card in cards.json:
            resulted_cards.append(self.create_card(card))
        return resulted_cards
