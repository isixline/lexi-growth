import pandas as pd
from lexi_growth.utils.file_util import get_result_file_path, get_known_list_file_path

def merge_known_word_to_known_list(result_file_path, known_list_file_path):
    result_df = pd.read_csv(result_file_path)
    assert 'word' in result_df.columns
    assert 'known' in result_df.columns

    known_list_df = pd.read_csv(known_list_file_path)
    assert 'word' in known_list_df.columns

    # get known words from result_df
    known_words_to_add = result_df[result_df['known'] == 1]
    assert 'word' in known_words_to_add.columns

    # merge known_words_to_add to known_list_df and remove duplicates
    known_list_df = pd.concat([known_list_df, known_words_to_add], ignore_index=True).drop_duplicates()
    assert 'word' in known_list_df.columns

    # sort known_list_df by word
    known_list_df.sort_values(by='word', inplace=True)
    assert 'word' in known_list_df.columns

    # filter known_list_df to have only 'word' column
    known_list_df = known_list_df[['word']]
    assert known_list_df.columns.tolist() == ['word']

    # save known_list_df to known_list_file_path
    known_list_df.to_csv(known_list_file_path, index=False)


def handle_word_merge_to_known_list():
    result_file_path = get_result_file_path()
    known_list_file_path = get_known_list_file_path()
    merge_known_word_to_known_list(result_file_path, known_list_file_path)
    return known_list_file_path