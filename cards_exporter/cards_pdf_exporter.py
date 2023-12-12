import pdfkit
from jinja2 import Environment, FileSystemLoader
from typing import List, Dict, NoReturn, Any
from entities.card import Card
from cards_exporter.icardexporter import ICardExporter
from utils.configuration_keys import ConfigurationKeys
from utils.icard_splitter import ICardsSplitter, Page


class CardPdfExporter(ICardExporter):

    def __init__(self, configuration: Dict[str, Any], splitter: ICardsSplitter):
        self._env = Environment(loader=FileSystemLoader('.'))
        self._configuration = configuration
        self._cards_splitter = splitter

    def export_cards(self, cards: List[Card], output_path: str) -> NoReturn:
        pages: List[Page] = self._cards_splitter.split_cards(cards)
        rendered_cards = self.render_cards_template(pages)
        self.write_cards_to_file(rendered_cards, output_path)

    def render_cards_template(self, pages: List[Page]) -> str:
        template_file_path: str = self._configuration[ConfigurationKeys.TEMPLATE_FILE_PATH_KEY]
        template = self._env.get_template(template_file_path)
        return template.render(pages=pages)

    def write_cards_to_file(self, rendered_cards: str, output_path: str) -> NoReturn:
        style_files_paths = self._configuration[ConfigurationKeys.STYLE_FILES_KEY]
        pdfkit.from_string(rendered_cards, output_path, css=style_files_paths)
