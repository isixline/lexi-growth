def compare_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        content1 = file1.read()
        content2 = file2.read()
        if content1 == content2:
            return True
        else:
            return False