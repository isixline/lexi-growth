import pandas as pd
import os
from lexi_growth.utils.file_util import converte_to_workspace_process_file_path

def handle_filter_known_word(word_list_path):
    known_list_file_path = os.getenv('KNOWN_LIST_FILE_PATH')
    known_list = pd.read_csv(known_list_file_path)
    word_list = pd.read_csv(word_list_path)

    # filtered_word_list is in word_list but not in known_list
    filtered_word_list = word_list[~word_list['word'].isin(known_list['word'])]

    output_path = converte_to_workspace_process_file_path('word_list_filtered', 'csv')
    filtered_word_list.to_csv(output_path, index=False)

    return output_path
