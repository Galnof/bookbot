import sys
from stats import (
    count_words, 
    chars_dict_to_sorted_list, 
    count_characters
)

# Coordinates the book analysis process and prints the final report.
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book(book_path)
    word_count = count_words(book)
    chars_dict = count_characters(book)
    chars_list = chars_dict_to_sorted_list(chars_dict)
    write_report(word_count, chars_list, book_path)

# Opens and returns the contents of a book as a string given its file path.
def get_book(path):

    with open(path) as f:
        return f.read()

# Generates a formatted report string containing:
# - The total word count
# - Character frequency counts (alphabetical chars only)
# - Sorted in descending order by frequency
def write_report(word_count, chars_list, book_path):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dictionary in chars_list:
        print(f"{dictionary["character"]}: {dictionary["char_count"]}")
    print("============= END ===============")

main()
