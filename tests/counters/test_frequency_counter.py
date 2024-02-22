from lexi_growth.counters.frequency_counter import count_words_from_file, handle_counte_words_by_frequency
from tests.test_utils.file_compare_util import compare_files
import os

def test_count_words_from_file():
    # given 
    file_path = "tests/test_data/counte_words.txt"

    # when
    word_count = count_words_from_file(file_path)

    # then
    assert word_count == {'hello': 3, 'python': 1, 'world': 2}

def test_handle_counte_words_by_frequency():
    # given
    file_path = "tests/test_data/counte_words.txt"
    expected_file_path = "tests/test_data/counte_words_by_frequency_expected.csv"

    # when
    output_file_path = handle_counte_words_by_frequency(file_path)

    # then
    compare_files(output_file_path, expected_file_path)
    os.remove(output_file_path)