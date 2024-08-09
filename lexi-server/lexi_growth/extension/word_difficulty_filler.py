from lexi_growth.core.word_filler import WordFiller
from lexi_growth.utils.word_difficulty_util import evaluate_word_difficulty

class WordDifficultyFiller(WordFiller):
    def fill(self, word_item):
        word = word_item.word
        difficulty = evaluate_word_difficulty(word)
        word_item.difficulty = difficulty
        return word_item