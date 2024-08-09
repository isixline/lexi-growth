from lexi_growth.core.lexi_flow import lexi_filter_flow
from lexi_growth.extension.word_frequency_counter import WordFrequencyCounter
from lexi_growth.extension.word_known_filter import KnownWordFilter
from lexi_growth.extension.word_definition_filler import WordDefinitionFiller
from lexi_growth.extension.word_translation_filler import WordTranslationFiller
from lexi_growth.extension.word_difficulty_filler import WordDifficultyFiller
from lexi_growth.core.word_filler import CombinedWordFiller
from lexi_growth.application.known_list_context import get_known_list, merge_to_known_list, remove_from_known_list

def handle_lexi_flow(text):
    word_counter = WordFrequencyCounter()
    word_filter = KnownWordFilter(get_known_list())
    word_filler = CombinedWordFiller([WordDefinitionFiller(), WordTranslationFiller(), WordDifficultyFiller()])
    return lexi_filter_flow(text, word_counter, word_filter, word_filler)

def handle_lexi_merge_to_known(word):
    merge_to_known_list(word)

def handle_lexi_revert_word(word):
    remove_from_known_list(word)