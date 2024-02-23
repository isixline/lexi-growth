from lexi_growth.handlers.merge_handler import merge_known_word_to_known_list
from tests.test_utils.file_compare_util import compare_files
from tests.test_utils.file_create_util import create_csv_file
import os

def test_merge_known_word_to_known_list():
    # given
    result_file_path = "tests/handlers/test_data/result.csv"
    known_list_file_path = "tests/handlers/test_data/known_list.csv"
    create_csv_file(known_list_file_path, ["word"], ["hello"])
    expected_file_path = "tests/handlers/test_data/known_list_expected.csv"
    
    # when
    merge_known_word_to_known_list(result_file_path, known_list_file_path)
    
    # then
    compare_files(known_list_file_path, expected_file_path)
    os.remove(known_list_file_path)