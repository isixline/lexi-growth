from googletrans import Translator
import pandas as pd
from lexi_growth.utils.file_util import converte_to_workspace_process_file_path

def get_word_chinese_translation(word):
    translator = Translator()

    translation = translator.translate(word, src='en', dest='zh-cn')

    translated_word = translation.text

    return translated_word

def apply_translate_for_file(file_path, translate_function):
    df = pd.read_csv(file_path)
    
    df['chinese_translation'] = df['word'].apply(translate_function)
    
    output_path = converte_to_workspace_process_file_path('word_list_chinese_translated', 'csv')

    df.to_csv(output_path, index=False)

    return output_path

def handle_translate_english_chinese(file_path):
    return apply_translate_for_file(file_path, get_word_chinese_translation)


