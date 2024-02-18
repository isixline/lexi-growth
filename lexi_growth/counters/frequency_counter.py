import re
import csv
import os

def count_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    text = re.sub(r'[^a-z ]', ' ', text)
    words = text.split()

    word_count = {}
    for word in words:
        if len(word) > 1: 
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

def process_file(word_count, file_path):
    sorted_result = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Word', 'Frequency']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word, count in sorted_result:
            writer.writerow({'Word': word, 'Frequency': count})

def handle_counte_words_by_frequency(file_path):
    word_count = count_words_from_file(file_path)
    output_file_path = file_path + ".csv"
    process_file(word_count, output_file_path)

    return output_file_path