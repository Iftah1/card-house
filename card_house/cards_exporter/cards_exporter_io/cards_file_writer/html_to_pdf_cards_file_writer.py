import os
from typing import Dict, Any, List, NoReturn
import pdfkit
from card_house.cards_exporter.cards_exporter_configuration.configuration_keys import ConfigurationKeys
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.icards_file_writer import ICardsFileWriter


class HtmlToPdfCardsFileWriter(ICardsFileWriter):
    def __init__(self, configuration: Dict[str, Any]):
        self._configuration = configuration

    def write_cards_to_file(self, rendered_cards: str, output_path: str) -> NoReturn:
        html_to_pdf_convertor_exe_path = self._configuration[ConfigurationKeys.HTML_TO_PDF_CONVERTOR_EXE_FILE]
        convertor_config = pdfkit.configuration(wkhtmltopdf= html_to_pdf_convertor_exe_path)
        pdfkit.from_string(rendered_cards, output_path, css=self.get_style_files(), configuration=convertor_config)

    def get_style_files(self) -> List[str]:
        style_files_paths = self._configuration[ConfigurationKeys.STYLE_FILES_KEY]
        return [os.path.join(directory, file) for directory, _, files in os.walk(style_files_paths) for file in files]
