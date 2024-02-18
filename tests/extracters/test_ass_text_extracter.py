import os
from lexi_growth.extracters.ass_text_extracter import extract_subtitles_from_ass, write_subtitles_to_text, extract_ass_text
from tests.utils.file_compare_util import compare_files

def test_extract_subtitles_from_ass():
    # given
    ass_file_path = "tests/test_data/Friends.S01E01.ass"

    # when
    subtitles = extract_subtitles_from_ass(ass_file_path)

    # then
    assert len(subtitles) == 401
    assert subtitles[1] == "中央咖啡馆"
    assert subtitles[2] == "There's nothing to tell!\n这没什么好说的"

def test_write_subtitles_to_text():
    # given
    subtitles = ["subtitle1", "subtitle2"]
    output_file_path = "tests/test_data/handled.txt"
    expected_file_path = "tests/test_data/test_write_subtitles_to_text_expected.txt"

    # when
    write_subtitles_to_text(subtitles, output_file_path)

    # then
    compare_files(output_file_path, expected_file_path)
    os.remove(output_file_path)

def test_extract_ass_text():
    # given
    ass_file_path = "tests/test_data/Friends.S01E01.ass"
    expected_output_file_path = "tests/test_data/Friends.S01E01.ass.txt"
    expected_file_path = "tests/test_data/test_extract_ass_text_expected.txt"

    # when
    extract_ass_text(ass_file_path)

    # then
    compare_files(expected_output_file_path, expected_file_path)
    os.remove(expected_output_file_path)






    
    