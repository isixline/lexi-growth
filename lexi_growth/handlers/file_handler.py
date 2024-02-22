from lexi_growth.extracters.extract_distributor import handle_extract_file_text
from lexi_growth.counters.frequency_counter import handle_counte_words_by_frequency
from lexi_growth.filters.known_word_filter import handle_filter_known_word
from lexi_growth.translators.english_english_translator import handle_translate_english_english
from lexi_growth.utils.file_util import copy_file
import os

def export_result_file(file_path):
    workspace_path = os.getenv('WORKSPACE_PATH')
    result_file_path = f"{workspace_path}/result.csv" 
    copy_file(file_path, result_file_path)
    return result_file_path

def handle_file(file_path):
    processing_functions = [
        handle_extract_file_text,
        handle_counte_words_by_frequency,
        handle_filter_known_word,
        handle_translate_english_english
    ]

    for func in processing_functions:
        file_path = func(file_path)

    result_file_path = export_result_file(file_path)
    return result_file_path