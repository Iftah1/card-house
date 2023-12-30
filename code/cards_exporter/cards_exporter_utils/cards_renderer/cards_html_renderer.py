from code.cards_exporter.cards_exporter_configuration.configuration_keys import ConfigurationKeys
from code.cards_exporter.cards_exporter_utils.cards_renderer.icards_renderer import ICardsRenderer
from code.cards_exporter.cards_exporter_utils.cards_splitter.icards_splitter import Page
from typing import List, Dict, Any
from jinja2 import Environment, FileSystemLoader


class CardsHtmlRenderer(ICardsRenderer):

    def __init__(self, configuration: Dict[str, Any]):
        self._env = Environment(loader=FileSystemLoader('.'))
        self._configuration = configuration

    def render_cards(self, cards_in_pages: List[Page]) -> str:
        template_file_path = self._configuration[ConfigurationKeys.TEMPLATE_FILE_PATH_KEY]
        template = self._env.get_template(template_file_path)
        return template.render(pages=cards_in_pages)
