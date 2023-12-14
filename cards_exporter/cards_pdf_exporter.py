import pdfkit
from jinja2 import Environment, FileSystemLoader
from typing import List, Dict, NoReturn, Any
from entities.card import Card
from cards_exporter.icardexporter import ICardExporter
from utils.configuration_keys import ConfigurationKeys

Row = List[Card]


class CardPdfExporter(ICardExporter):

    def __init__(self, configuration: Dict[str, Any]):
        self._env = Environment(loader=FileSystemLoader('.'))
        self._configuration = configuration

    def export_cards(self, cards: List[Card], output_path: str) -> NoReturn:
        cards_in_rows = self.split_cards_to_rows(cards)
        rendered_cards = self.render_cards_template(cards_in_rows)
        self.write_cards_to_file(rendered_cards, output_path)

    def split_cards_to_rows(self, cards: List[Card]) -> List[Row]:
        cards_in_row: int = self._configuration[ConfigurationKeys.NUM_CARDS_IN_ROW_KEY]
        for i in range(0, len(cards), cards_in_row):
            yield cards[i: min(i + cards_in_row, len(cards))]

    def render_cards_template(self, cards: List[Row]) -> str:
        template_file_path: str = self._configuration[ConfigurationKeys.TEMPLATE_FILE_PATH_KEY]
        template = self._env.get_template(template_file_path)
        return template.render(rows=cards)

    def write_cards_to_file(self, rendered_cards: str, output_path: str) -> NoReturn:
        style_files_paths = self._configuration[ConfigurationKeys.STYLE_FILES_KEY]
        pdfkit.from_string(rendered_cards, output_path, css=style_files_paths)
