from lexi_growth.extracters.extract_distributor import handle_extract_file_text
from lexi_growth.counters.frequency_counter import handle_counte_words_by_frequency
from lexi_growth.filters.known_word_filter import handle_filter_known_word
from lexi_growth.translators.english_english_translator import handle_translate_english_english
from lexi_growth.translators.english_chinese_translator import handle_translate_english_chinese
from lexi_growth.utils.file_util import copy_file, converte_to_workspace_process_file_path
import os

def export_result_file(file_path):
    workspace_path = os.getenv('WORKSPACE_PATH')
    result_file_path = f"{workspace_path}/result.csv" 
    copy_file(file_path, result_file_path)
    return result_file_path

def handle_word_filter(**kwargs):
    file_path = kwargs.get("file_path")
    handles = kwargs.get("handles").split(",") if kwargs.get("handles") else []

    handle_functions = [
        {"function": handle_translate_english_english, "handle": "english_definition"},
        {"function": handle_translate_english_chinese, "handle": "chinese_translation"},
    ]

    file_path = handle_extract_file_text(file_path, kwargs.get("index"))
    file_path = handle_counte_words_by_frequency(file_path)
    file_path = handle_filter_known_word(file_path)

    file_path = copy_file(file_path, converte_to_workspace_process_file_path("word_list_handled", "csv"))
    max_words = int(kwargs.get("max_words"))
    for func in handle_functions:
        if handles and func.get("handles") and func.get("handles") not in handles:
            continue
        try:
            file_path = func.get("function")(file_path, max_words)
        except: 
            print(f"Error in {func.get('function')}")
            pass

    export_result_file(file_path)