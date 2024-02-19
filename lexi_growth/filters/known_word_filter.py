import pandas as pd
import os

def handle_filter_known_word(word_list_path, output_path):
    known_list_file_path = os.getenv('KNOWN_LIST_FILE_PATH')
    known_list = pd.read_csv(known_list_file_path)
    word_list = pd.read_csv(word_list_path)

    # filtered_word_list is in word_list but not in known_list
    filtered_word_list = word_list[~word_list['word'].isin(known_list['word'])]


    filtered_word_list.to_csv(output_path, index=False)
