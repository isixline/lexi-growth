from lexi_growth.core.word_counter import WordCounter
from lexi_growth.core.word_filter import WordFilter
from lexi_growth.core.word_filler import WordFiller

def lexi_filter_flow(text: str, count_word: WordCounter, filter_word: WordFilter, fill_word: WordFiller):
    word_items = count_word.count(text)
    print('word count done')
    word_items = filter_word.filter(word_items)
    print('word filter done')
    word_items = fill_word.fill_list(word_items)
    print('word fill done')
    return word_items