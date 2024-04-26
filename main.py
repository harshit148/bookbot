import os
import argparse

def main():
    parser = argparse.ArgumentParser(prog='BookBot', 
                                    description='Get word count and character counts of a book')
    parser.add_argument('-b', '--bookname', 
                        dest='book_name',
                        help='Name of the book(should be present in books directory)',
                        required=True,
                        default='frankenstein.txt')
    args = parser.parse_args()
    print(f'--- Begin report of books/{args.book_name} ---')
    book_path = f'books/{args.book_name}'
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    print(f'{num_words} words found in the book\n')
    characters = get_character_count(book_contents)
    print_character_report(characters)


def get_num_words(file_contents: str) -> int:
    return len(file_contents.split())


def get_book_text(book_path: str) -> str:
    with open(os.getcwd() + os.sep + book_path) as f:
        return f.read()

def get_character_count(file_contents: str) -> dict:
    file_contents = file_contents.lower()
    character_count = {}
    for ch in file_contents:
        if ch.isalpha():
            character_count[ch] = 1 + character_count.get(ch, 0)
    return character_count


def print_character_report(characters: dict) -> None:
    for ch, count in characters.items():
        print(f"The {ch} character was found {count} times")


if __name__ == "__main__":
    main()