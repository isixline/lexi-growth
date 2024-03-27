from abc import ABC, abstractmethod
from lexi_growth.core.word_item import WordItem

class WordFiller(ABC):
    @abstractmethod
    def fill(self, word_item: WordItem) -> WordItem:
        pass

    def fill_list(self, word_items: list[WordItem]) -> list[WordItem]:
        return [self.fill(word_item) for word_item in word_items]

class CombinedWordFiller(WordFiller):
    def __init__(self, word_fillers: list[WordFiller] = []):
        self.word_fillers = word_fillers

    def add_word_filler(self, word_filler):
        self.word_fillers.append(word_filler)

    def fill(self, word_item: WordItem) -> WordItem:
        for word_filler in self.word_fillers:
            word_item = word_filler.fill(word_item)
        return word_item