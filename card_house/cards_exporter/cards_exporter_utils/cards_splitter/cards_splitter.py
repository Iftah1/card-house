from typing import List, Dict, Any
from card_house.cards_exporter.cards_exporter_configuration.configuration_keys import ConfigurationKeys
from card_house.cards_exporter.cards_exporter_entities.printed_card import PrintedCard, Page
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.icards_splitter import ICardsSplitter
from card_house.cards_exporter.cards_exporter_utils.printed_cards_creator.iprinted_cards_creator import IPrintedCardsCreator
from card_house.infrastructure.entities.card import Card

PageWithoutRows = List[PrintedCard]


class CardsSplitter(ICardsSplitter):

    def __init__(self, configuration: Dict[str, Any], printed_cards_creator: IPrintedCardsCreator):
        self._configuration = configuration
        self._printed_cards_creator = printed_cards_creator

    def split_cards(self, cards: List[Card]) -> List[Page]:
        pages_without_rows: List[PageWithoutRows] = self.split_cards_to_pages_without_rows(cards)
        return self.split_pages_into_rows(pages_without_rows)

    def split_cards_to_pages_without_rows(self, cards: List[Card]) -> List[PageWithoutRows]:
        cards_in_page = self.get_num_of_cards_in_page()
        for i in range(0, len(cards), cards_in_page):
            yield self._printed_cards_creator.create_printed_cards_from_cards(cards[i:i + cards_in_page])

    def get_num_of_cards_in_page(self) -> int:
        cards_in_row = self._configuration[ConfigurationKeys.NUM_CARDS_IN_ROW_KEY]
        rows_in_page = self._configuration[ConfigurationKeys.NUM_ROWS_IN_PAGE_KEY]
        return rows_in_page * cards_in_row

    def split_pages_into_rows(self, pages: List[PageWithoutRows]) -> List[Page]:
        cards_in_row = self._configuration[ConfigurationKeys.NUM_CARDS_IN_ROW_KEY]
        for page in pages:
            yield [page[i: i + cards_in_row] for i in range(0, len(page), cards_in_row)]
