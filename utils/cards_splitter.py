from entities.card import Card
from typing import List, Dict, Any, TypeVar
from configuration_keys import ConfigurationKeys
from icard_splitter import ICardsSplitter, Page, Row

T = TypeVar("T")


def split_list(lst: List[T], split_size: int) -> List[List[T]]:
    for i in range(0, len(lst), split_size):
        yield lst[i:i + split_size]


class CardsSplitter(ICardsSplitter):

    def __init__(self, configuration: Dict[str, Any]):
        self._cards_in_row = configuration[ConfigurationKeys.NUM_CARDS_IN_ROW_KEY]
        self._rows_in_page = configuration[ConfigurationKeys.NUM_ROWS_IN_PAGE_KEY]

    def split_cards(self, cards: List[Card]) -> List[Page]:
        cards_in_rows: List[Row] = split_list(cards, self._cards_in_row)
        return split_list(cards_in_rows, self._rows_in_page)
