from entities.card import Card
from typing import List, Dict, Any
from utils.configuration_keys import ConfigurationKeys
from utils.icard_splitter import ICardsSplitter, Page

PageWithoutRows = List[Card]


class CardsSplitter(ICardsSplitter):

    def __init__(self, configuration: Dict[str, Any]):
        self._cards_in_row = configuration[ConfigurationKeys.NUM_CARDS_IN_ROW_KEY]
        self._rows_in_page = configuration[ConfigurationKeys.NUM_ROWS_IN_PAGE_KEY]

    def split_cards(self, cards: List[Card]) -> List[Page]:
        pages_without_rows: List[PageWithoutRows] = self.split_cards_to_pages_without_rows(cards)
        return self.split_pages_into_rows(pages_without_rows)

    def split_cards_to_pages_without_rows(self, cards: List[Card]) -> List[PageWithoutRows]:
        cards_in_page: int = self._rows_in_page * self._cards_in_row
        for i in range(0, len(cards), cards_in_page):
            yield cards[i:i + cards_in_page]

    def split_pages_into_rows(self, pages: List[PageWithoutRows]) -> List[Page]:
        for page in pages:
            yield [page[i: i + self._cards_in_row] for i in range(0, len(page), self._cards_in_row)]
