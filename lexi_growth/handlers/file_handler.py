from lexi_growth.extracters.ass_text_extracter import handle_extract_ass_text
from lexi_growth.counters.frequency_counter import handle_counte_words_by_frequency
from lexi_growth.filters.known_word_filter import handle_filter_known_word

def handle_file_type(file_path):
    if file_path.lower().endswith('.ass'):
        return handle_extract_ass_text(file_path)
    else:
        return file_path

def handle_file(file_path):
    processing_functions = [
        handle_file_type,
        handle_counte_words_by_frequency,
        handle_filter_known_word
    ]

    for func in processing_functions:
        file_path = func(file_path)

    return file_path