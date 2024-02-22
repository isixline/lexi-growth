from lexi_growth.extracters.ass_text_extracter import handle_extract_ass_text

def handle_extract_file_text(file_path):
    if file_path.lower().endswith('.ass'):
        return handle_extract_ass_text(file_path)
    else:
        return file_path