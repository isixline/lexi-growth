from lexi_growth.core.word_filler import WordFiller
from dict_toolkit.extensions.query_agent import auto_query

class WordDefinitionFiller(WordFiller):
    def fill(self, word_item):
        word = word_item.word
        lexical_item = auto_query(word)
        word_item.definition = lexical_item.definition if lexical_item else 'Not found'
        return word_item