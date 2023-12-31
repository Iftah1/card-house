from abc import ABC, abstractmethod
from typing import NoReturn


class ICardsFileWriter(ABC):
    @abstractmethod
    def write_cards_to_file(self, rendered_cards: str, output_path: str) -> NoReturn:
        raise NotImplementedError
