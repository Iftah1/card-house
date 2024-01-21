from abc import ABC, abstractmethod
from typing import List
from card_house.infrastructure.entities.card import Card

'''
TODO: Consider in the future to make this abstract class instead of interface, with only `create_card` method as 
abstract method. The logic of  `create_cards` should be constant.
'''


class ICardsCreator(ABC):

    @abstractmethod
    def create_card(self, card: Card) -> Card:
        raise NotImplementedError

    @abstractmethod
    def create_cards(self, cards: List[Card]) -> List[Card]:
        raise NotImplementedError
