from abc import ABC, abstractmethod
from lexi_growth.core.word_item import WordItem

class WordCounter(ABC):
    @abstractmethod
    def count(self, text: str) -> list[WordItem]:
        pass
