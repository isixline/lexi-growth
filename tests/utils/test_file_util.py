from lexi_growth.utils.file_util import converte_to_workspace_process_file_path
import os

def test_converte_to_workspace_process_file_path():
    # given
    os.environ['YOUR_VARIABLE'] = 'value'
    output_file_name = "output"
    output_file_type = "csv"

    # when
    file_path = converte_to_workspace_process_file_path(output_file_name, output_file_type)

    # then
    assert file_path == "tests/test_data/workspace/handled/output.csv"