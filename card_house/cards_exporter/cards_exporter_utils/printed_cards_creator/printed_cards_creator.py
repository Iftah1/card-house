from typing import List, Dict, Any
from card_house.cards_exporter.cards_exporter_configuration.configuration_keys import ConfigurationKeys
from card_house.cards_exporter.cards_exporter_entities.printed_card import PrintedCard
from card_house.cards_exporter.cards_exporter_utils.printed_cards_creator.iprinted_cards_creator import IPrintedCardsCreator
from card_house.infrastructure.entities.card import Card
from card_house.infrastructure.entities.card_type import CardType


class PrintedCardsCreator(IPrintedCardsCreator):

    def __init__(self, configuration: Dict[str, Any]):
        self._configuration = configuration

    def create_printed_cards_from_cards(self, cards: List[Card]) -> List[PrintedCard]:
        return [PrintedCard(card.content, self._configuration[self.get_design_properties_configuration_key(card.type)])
                for card in cards]

    @staticmethod
    def get_design_properties_configuration_key(card_type: CardType) -> str:
        return ConfigurationKeys.QUESTION_DESIGN_PROPERTIES_KEY if card_type == CardType.QUESTION \
            else ConfigurationKeys.ANSWER_DESIGN_PROPERTIES_KEY
