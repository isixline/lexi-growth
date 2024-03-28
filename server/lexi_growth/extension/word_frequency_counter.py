import re
from lexi_growth.core.word_counter import WordCounter
from lexi_growth.core.word_item import WordItem

class WordFrequencyCounter(WordCounter):
    def count(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z ]', ' ', text)
        words = text.split()

        word_count = {}
        for word in words:
            if len(word) > 1: 
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        return [WordItem(word, count, None, None) for word, count in word_count.items()]
