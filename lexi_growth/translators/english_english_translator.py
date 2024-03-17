import pandas as pd
import requests
from dict_toolkit.extensions.query_agent import auto_query

def get_word_english_definition(word):
    print(f"Getting definition for {word}")
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            definitions = [definition['definition'] for entry in data for meaning in entry.get('meanings', []) for definition in meaning.get('definitions', [])]
            return '; '.join(definitions[:1])
        else:
            return 'Not found'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'Error'
    
def get_word_english_definition_by_dict(word):
    lexical_item = auto_query(word)
    print(f"Getting definition for {word}")
    return lexical_item.definition if lexical_item else 'Not found'
    
def apply_translate_for_file(file_path, max_words, translate_function):
    df = pd.read_csv(file_path)
    
    if max_words:
        df = df.head(max_words)
    df['english_definition'] = df['word'].apply(translate_function)
    
    df.to_csv(file_path, index=False)
    
    return file_path

    
def handle_translate_english_english(file_path, max_words):
    return apply_translate_for_file(file_path, max_words, get_word_english_definition_by_dict)