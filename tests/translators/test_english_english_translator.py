from lexi_growth.translators.english_english_translator import get_word_english_definition, apply_translate_for_file
from tests.mocks.dictionaryapi_mock import mock_dictionaryapi_get_entries_en_success, mock_dictionaryapi_get_entries_en_success_multiple_definitions, mock_dictionaryapi_get_entries_en_not_found, mock_dictionaryapi_get_entries_en_error
from tests.test_utils.file_compare_util import compare_files
import os

def test_get_word_english_definition_success(mock_dictionaryapi_get_entries_en_success):
    # given
    word = "cat"

    # when
    definition = get_word_english_definition(word)

    # then
    assert definition == "a domesticated carnivorous mammal that originated from wolves"

def test_get_word_english_definition_success_multiple_definitions(mock_dictionaryapi_get_entries_en_success_multiple_definitions):
    # given
    word = "cat"

    # when
    definition = get_word_english_definition(word)

    # then
    assert definition == "a domesticated carnivorous mammal that originated from wolves; a small domesticated carnivorous mammal with soft fur"

def test_get_word_english_definition_not_found(mock_dictionaryapi_get_entries_en_not_found):
    # given
    word = "cat"

    # when
    definition = get_word_english_definition(word)

    # then
    assert definition == "Not found"

def test_get_word_english_definition_error(mock_dictionaryapi_get_entries_en_error):
    # given
    word = "cat"

    # when
    definition = get_word_english_definition(word)

    # then
    assert definition == "Error"

def test_apply_translate_for_file():
    # given
    word_list_path = "tests/test_data/word_list.csv"
    expected_file_path = "tests/test_data/word_list_english_translated_expected.csv"
    translate_function = lambda word: f"{word}_translated"

    # when
    output_path = apply_translate_for_file(word_list_path, translate_function)

    # then
    compare_files(output_path, expected_file_path)
    os.remove(output_path)