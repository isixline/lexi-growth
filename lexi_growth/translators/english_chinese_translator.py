from googletrans import Translator
import pandas as pd
from dict_toolkit.extensions.query_agent import auto_query

def get_word_chinese_translation(word):
    translator = Translator()

    translation = translator.translate(word, src='en', dest='zh-cn')

    translated_word = translation.text

    return translated_word

def get_word_chinese_translation_by_dict(word):
    lexical_item = auto_query(word)
    print(f"Getting translation for {word}")
    return lexical_item.translation if lexical_item else 'Not found'

def apply_translate_for_file(file_path, max_words, translate_function):
    df = pd.read_csv(file_path)
    
    if max_words:
        df = df.head(max_words)
    # add new column chinese_translation
    df['chinese_translation'] = df['word'].apply(translate_function)

    # output to file_path
    df.to_csv(file_path, index=False)

    return file_path

def handle_translate_english_chinese(file_path, max_words):
    return apply_translate_for_file(file_path, max_words, get_word_chinese_translation_by_dict)


