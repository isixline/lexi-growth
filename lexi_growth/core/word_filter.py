from abc import ABC, abstractmethod
from lexi_growth.core.word_item import WordItem

class WordFilter(ABC):
    @abstractmethod
    def filter(self, word_items: list[WordItem]) -> list[WordItem]:
        pass
    