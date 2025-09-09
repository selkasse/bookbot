from stats import get_num_words, count_characters, sort_by_character
import sys

def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_report(filepath, word_count, sorted_characters):
    report_string = '============ BOOKBOT ============\n'
    report_string += 'Analyzing book found at ' + filepath + '...\n'
    report_string += '----------- Word Count ----------\n'
    report_string += f'Found {word_count} total words\n'
    report_string += '--------- Character Count -------\n'


    for character_dict in sorted_characters:
        character = character_dict["character"]
        count = character_dict["num"]

        if character.isalpha():
            report_string += f'{character}: {count}\n'

    print(report_string)

def parse_args(args):
    if len(args) != 2:
        print('Usage: python3 main.py <path_to_book>')
        print('example: python3 main.py books/frankenstein.txt')
        sys.exit(1)
    else:
        return args[1]



def main():
    #filepath = 'books/frankenstein.txt'
    filepath = parse_args(sys.argv)
    frankenstein = get_book_text(filepath)
    word_count = get_num_words(frankenstein)
    character_counts = count_characters(frankenstein)
    sorted_characters = sort_by_character(character_counts) 

    print_report(filepath, word_count, sorted_characters)
main()
