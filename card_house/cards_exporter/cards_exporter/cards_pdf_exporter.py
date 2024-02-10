from typing import List, NoReturn
from card_house.cards_exporter.cards_exporter_entities.printed_card import Page
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.icards_file_writer import ICardsFileWriter
from card_house.cards_exporter.cards_exporter_utils.cards_renderer.icards_renderer import ICardsRenderer
from card_house.infrastructure.entities.card import Card
from card_house.cards_exporter.cards_exporter.icards_exporter import ICardsExporter
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.icards_splitter import ICardsSplitter


class CardsPdfExporter(ICardsExporter):

    def __init__(self, cards_splitter: ICardsSplitter, cards_renderer: ICardsRenderer,
                 cards_file_writer: ICardsFileWriter):
        self._cards_splitter = cards_splitter
        self._cards_renderer = cards_renderer
        self._cards_file_writer = cards_file_writer

    def export_cards(self, cards: List[Card], output_path: str) -> NoReturn:
        cards_in_pages: List[Page] = self._cards_splitter.split_cards(cards)
        rendered_cards: str = self._cards_renderer.render_cards(cards_in_pages)
        self._cards_file_writer.write_cards_to_file(rendered_cards, output_path)
