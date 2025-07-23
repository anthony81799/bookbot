def get_num_words(book_text):
    return len(book_text.split())


def get_char_count(book_text):
    char_counts = {}
    for char in book_text.lower():
        if char in char_counts:
            char_counts[char] += 1
            continue
        char_counts[char] = 1
    return char_counts


def sort_chars(char_counts):
    sorted = []
    for char in char_counts:
        sorted.append({"char": char, "num": char_counts[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def sort_on(items):
    return items["num"]
