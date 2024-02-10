from typing import List, Dict, Any
from card_house.cards_exporter.cards_exporter_configuration.configuration_keys import ConfigurationKeys
from card_house.cards_exporter.cards_exporter_entities.printed_card import PrintedCard
from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.entities.card import Card
from card_house.infrastructure.entities.card_type import CardType


class PrintedCardsCreator(ICardsCreator):

    def __init__(self, configuration: Dict[str, Any]):
        self._configuration = configuration

    def create_card(self, card: Card) -> Card:
        design_properties: Dict[str, str] = self.get_design_properties(card.type)
        return PrintedCard(
            content=card.content,
            type=card.type,
            title=design_properties["title"],
            sign=design_properties["sign"],
            design_id=design_properties["design_id"])

    def create_cards(self, cards: List[Card]) -> List[Card]:
        return [self.create_card(card) for card in cards]

    def get_design_properties(self, card_type: CardType) -> Dict[str, str]:
        return self._configuration[self.get_design_properties_configuration_key(card_type)]

    @staticmethod
    def get_design_properties_configuration_key(card_type: CardType) -> str:
        return ConfigurationKeys.QUESTION_DESIGN_PROPERTIES_KEY if card_type == CardType.QUESTION \
            else ConfigurationKeys.ANSWER_DESIGN_PROPERTIES_KEY
