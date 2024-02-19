import sys
from dotenv import load_dotenv
from lexi_growth.handlers.file_handler import handle_file

def main():
    load_dotenv()

    file_path = sys.argv[1]

    processed_file_path = handle_file(file_path)
    print(f"Processed file: {processed_file_path}")
    

if __name__ == "__main__":
    main()
