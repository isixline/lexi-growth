import os
import shutil

def converte_to_workspace_process_file_path(output_file_name, output_file_type):
    workspace_path = os.getenv('WORKSPACE_PATH')
    directory = f"{workspace_path}/handled"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return f"{directory}/{output_file_name}.{output_file_type}"

def copy_file(source_file_path, target_file_path):
    shutil.copyfile(source_file_path, target_file_path)
    return target_file_path
