from stats import get_num_words, get_char_count, sort_chars
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = get_char_count(book_text)
    sorted = sort_chars(char_counts)
    for char in sorted:
        if not char["char"].isalpha:
            continue
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


main()
