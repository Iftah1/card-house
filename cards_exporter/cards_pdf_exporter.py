import pdfkit
from jinja2 import Environment, FileSystemLoader
from typing import List, NoReturn
from entities.card import Card
from cards_exporter.icardexporter import ICardExporter
from Utils.configuration_keys import ConfigurationKeys


class CardPdfExporter(ICardExporter):

    def __init__(self, configuration: dict):
        self._env = Environment(loader=FileSystemLoader('.'))
        self._configuration = configuration

    def export_cards(self, cards: List[Card], output_path: str) -> NoReturn:
        cards_in_rows = self.split_cards_to_rows(cards)
        rendered_cards = self.render_cards_template(cards_in_rows)
        self.write_cards_to_file(rendered_cards, output_path)

    def split_cards_to_rows(self, cards: List[Card]) -> List[List[Card]]:
        cards_in_row: int = self._configuration[ConfigurationKeys.NUM_CARDS_IN_ROW_KEY]
        for i in range(0, len(cards), cards_in_row):
            yield cards[i: min(i + cards_in_row, len(cards))]

    def render_cards_template(self, cards: List[List[Card]]) -> str:
        template_file_path: str = self._configuration[ConfigurationKeys.TEMPLATE_FILE_PATH_KEY]
        template = self._env.get_template(template_file_path)
        return template.render(rows=cards)

    def write_cards_to_file(self, cards: str, output_path: str):
        style_files_paths = self._configuration[ConfigurationKeys.STYLE_FILES_KEY]
        pdfkit.from_string(cards, output_path, css=style_files_paths)
