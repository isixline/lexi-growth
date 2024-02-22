import re
from lexi_growth.utils.file_util import converte_to_workspace_process_file_path

def extract_subtitles_from_ass(ass_file_path):
    subtitles = []
    with open(ass_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('Dialogue:'):
                parts = line.split(',', 9)
                subtitle = parts[9].strip()
                subtitle = re.sub(r'{\\[^}]+}', '', subtitle) 
                subtitle = subtitle.replace('\\N', '\n')
                subtitles.append(subtitle)
    return subtitles

def write_subtitles_to_text(subtitles, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for idx, subtitle in enumerate(subtitles, 1):
            file.write(f'{subtitle}\n')

def handle_extract_ass_text(ass_file_path):
    subtitles = extract_subtitles_from_ass(ass_file_path)
    output_file_path = converte_to_workspace_process_file_path("text", "txt")
    write_subtitles_to_text(subtitles, output_file_path)
    return output_file_path
