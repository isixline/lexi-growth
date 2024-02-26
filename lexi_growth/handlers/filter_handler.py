from lexi_growth.extracters.extract_distributor import handle_extract_file_text
from lexi_growth.counters.frequency_counter import handle_counte_words_by_frequency
from lexi_growth.filters.known_word_filter import handle_filter_known_word
from lexi_growth.translators.english_english_translator import handle_translate_english_english
from lexi_growth.translators.english_chinese_translator import handle_translate_english_chinese
from lexi_growth.utils.file_util import copy_file
import os

def export_result_file(file_path):
    workspace_path = os.getenv('WORKSPACE_PATH')
    result_file_path = f"{workspace_path}/result.csv" 
    copy_file(file_path, result_file_path)
    return result_file_path

def handle_word_filter(**kwargs):
    file_path = kwargs.get("file_path")
    handles = kwargs.get("handles").split(",") if kwargs.get("handles") else None
    print(f"handles: {handles}")

    processing_functions = [
        {"function": handle_extract_file_text},
        {"function": handle_counte_words_by_frequency},
        {"function": handle_filter_known_word},
        {"function": handle_translate_english_english, "handles": "english_definition"},
        {"function": handle_translate_english_chinese, "handles": "chinese_translation"},
    ]

    for func in processing_functions:
        if handles and func.get("handles") and func.get("handles") not in handles:
            continue
        file_path = func.get("function")(file_path)

    result_file_path = export_result_file(file_path)
    return result_file_path