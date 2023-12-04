from enum import Enum
from dataclasses import dataclass
from Utils.configuration_keys import ConfigurationKeys


class CardType(Enum):
    QUESTION = True,
    ANSWER = False

    def GetDesignPropertiesKey(self) -> str:
        return ConfigurationKeys.QUESTION_DESIGN_PROPERTIES_KEY if self == CardType.QUESTION \
            else ConfigurationKeys.ANSWER_DESIGN_PROPERTIES_KEY


@dataclass
class CardDesignProperties:
    title: str
    sign: str
    design_id: str

    def __init__(self, json_dict):
        self.title = json_dict["title"]
        self.sign = json_dict["sign"]
        self.design_id = json_dict["design_id"]
