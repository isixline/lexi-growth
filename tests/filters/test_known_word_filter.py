from lexi_growth.filters.known_word_filter import handle_filter_known_word
from tests.utils.file_compare_util import compare_files
import os
from dotenv import load_dotenv

def test_handle_filter_known_word():
    # given
    load_dotenv('tests/.env.test')
    word_list_path = "tests/test_data/word_list.csv"
    expected_file_path = "tests/test_data/filtered_word_list_expected.csv"

    # when
    output_path = handle_filter_known_word(word_list_path)

    # then
    compare_files(output_path, expected_file_path)
    os.remove(output_path)