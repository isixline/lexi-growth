import pandas as pd
import requests
from lexi_growth.utils.file_util import converte_to_workspace_process_file_path

def get_word_english_definition(word):
    print(f"Getting definition for {word}")
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            definitions = [definition['definition'] for entry in data for meaning in entry.get('meanings', []) for definition in meaning.get('definitions', [])]
            return '; '.join(definitions[:3])
        else:
            return 'Not found'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'Error'
    
def apply_translate_for_file(file_path, translate_function):
    df = pd.read_csv(file_path)
    
    df['english_definition'] = df['word'].apply(translate_function)
    
    df.to_csv(file_path, index=False)
    
    return file_path

    
def handle_translate_english_english(file_path):
    return apply_translate_for_file(file_path, get_word_english_definition)