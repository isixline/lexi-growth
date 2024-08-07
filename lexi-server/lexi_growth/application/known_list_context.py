import os
import pandas as pd
from lexi_growth.core.known_item import KnowItem

def get_known_list() -> list[KnowItem]:
    known_list_file_path = os.getenv('KNOWN_LIST_FILE_PATH')
    assert known_list_file_path is not None
    known_list = pd.read_csv(known_list_file_path)
    assert 'word' in known_list.columns
    return [KnowItem(row['word']) for index, row in known_list.iterrows()]

def merge_to_known_list(word: str):
    known_list_file_path = os.getenv('KNOWN_LIST_FILE_PATH')
    assert known_list_file_path is not None
    known_list_df = pd.read_csv(known_list_file_path)
    assert 'word' in known_list_df.columns

    known_words_to_add = pd.DataFrame( {'word': [word]})

    known_list_df = pd.concat([known_list_df, known_words_to_add], ignore_index=True).drop_duplicates()

    known_list_df.sort_values(by='word', inplace=True)
   
    known_list_df.to_csv(known_list_file_path, index=False)

def remove_from_known_list(word: str):
    known_list_file_path = os.getenv('KNOWN_LIST_FILE_PATH')
    assert known_list_file_path is not None
    known_list_df = pd.read_csv(known_list_file_path)

    if 'word' in known_list_df.columns:
        known_list_df = known_list_df[known_list_df.word != word]
        known_list_df.to_csv(known_list_file_path , index=False)
