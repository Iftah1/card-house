from enum import Enum
from Utils.configuration_keys import ConfigurationKeys


class CardType(Enum):
    QUESTION = True,
    ANSWER = False

    def GetDesignPropertiesKey(self) -> str:
        return ConfigurationKeys.QUESTION_DESIGN_PROPERTIES_KEY if self == CardType.QUESTION \
            else ConfigurationKeys.ANSWER_DESIGN_PROPERTIES_KEY
