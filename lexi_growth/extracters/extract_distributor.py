from lexi_growth.extracters.ass_text_extracter import handle_extract_ass_text
from lexi_growth.extracters.epub_text_extracter import handle_extract_epub_text

def handle_extract_file_text(file_path, index):
    if file_path.lower().endswith('.ass'):
        return handle_extract_ass_text(file_path)
    if file_path.lower().endswith('.epub'):
        return handle_extract_epub_text(file_path, index)
    
    return file_path