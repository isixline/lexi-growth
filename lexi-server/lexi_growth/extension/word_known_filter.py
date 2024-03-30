from lexi_growth.core.word_filter import WordFilter
from lexi_growth.core.known_item import KnowItem
from lexi_growth.core.word_item import WordItem
import pandas as pd

class KnownWordFilter(WordFilter):
    def __init__(self, known_list: list[KnowItem]):
        self.known_list = known_list

    def filter(self, word_items):
        pd_word_items = pd.DataFrame([{'word': item.word, 'count': item.count} for item in word_items])
        pd_known_items = pd.DataFrame([{'word': item.word} for item in self.known_list])
        filtered_word_list = pd_word_items[~pd_word_items['word'].isin(pd_known_items['word'])]
        return [WordItem(row['word'], row['count'], None, None) for index, row in filtered_word_list.iterrows()]