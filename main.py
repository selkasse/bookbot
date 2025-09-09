from stats import get_num_words, count_characters

def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
   #print(get_book_text('books/frankenstein.txt'))
   frankenstein = get_book_text('books/frankenstein.txt')
   #print(f"{get_num_words(frankenstein)} words found in the document")
   print(count_characters(frankenstein))

main()
