import pandas as pd
import os
from lexi_growth.utils.file_util import converte_to_workspace_process_file_path

def handle_filter_known_word(word_list_path):
    known_list_file_path = os.getenv('KNOWN_LIST_FILE_PATH')
    known_list = pd.read_csv(known_list_file_path)
    word_list = pd.read_csv(word_list_path)

    # filtered_word_list is in word_list but not in known_list
    filtered_word_list = word_list[~word_list['word'].isin(known_list['word'])]

    # Create a DataFrame with 'word' 'frequency' column from filtered_word_list
    output_df = pd.DataFrame(filtered_word_list, columns=['word', 'frequency'])

    # Add 'known' column with all values as 0
    output_df['known'] = 0

    # Reorder columns to have 'known' column as the first column
    output_df = output_df[['known', 'word', 'frequency']]

    output_path = converte_to_workspace_process_file_path('word_list_filtered', 'csv')
    output_df.to_csv(output_path, index=False)

    return output_path
