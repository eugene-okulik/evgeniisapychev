import argparse
import re
import os
from pathlib import Path


def print_file_content(filename, search_word):
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            word = re.findall(r'[^\s]+', line, flags=re.IGNORECASE)
            if search_word in word:
                num_word = word.index(search_word)
                num = max(0, num_word - 5)
                num2 = min(num_word + 6, len(word))
                context_word = word[num:num_word]
                context_word2 = word[num_word + 1:num2]
                context = ' '.join(context_word)
                context2 = ' '.join(context_word2)
                print(f'Файл {filename}, Строка {line_number}: ДО |{context}| {search_word.strip()} ПОСЛЕ |{context2}|')


def path_process(directory, search_word):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if file_path.is_file():
                print_file_content(file_path, search_word)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='directory name')
    parser.add_argument('-w', '--search_word', help='word for search', required=True)
    args = parser.parse_args()
    path = Path(args.directory)
    path_process(path, args.search_word)


if __name__ == '__main__':
    main()
