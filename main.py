from stats import get_word_count, char_count, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    word_count = get_word_count(get_book_text(book))
    print(f"{word_count} words found in the document")

    char = char_count(get_book_text(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in sort_dict(char):
        print(c)
    print("============= END ===============")
main()
