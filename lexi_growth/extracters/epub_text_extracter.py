import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from lexi_growth.utils.file_util import converte_to_workspace_process_file_path

def extract_text_from_epub(epub_file, index):
    book = epub.read_epub(epub_file)
    text = ""

    num_chapters = 0
    index=int(index)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            num_chapters += 1
            if (num_chapters == index):
                soup = BeautifulSoup(item.get_body_content(), 'html.parser')
                print("soup.get_text()", soup.get_text())
                return soup.get_text()

    return text

def handle_extract_epub_text(file_path, index):
    text = extract_text_from_epub(file_path, index)
    output_file_path = converte_to_workspace_process_file_path("text", "txt")
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return output_file_path

