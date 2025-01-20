# Coordinates the book analysis process and prints the final report.
def main():
	
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = count_words(book)
    chars_dict = count_characters(book)
    final_report = write_report(word_count, chars_dict)
    print(final_report)

# Opens and returns the contents of a book as a string given its file path.
def get_book(path):

    with open(path) as f:
        return f.read()

# Receives the book text and counts the amount of words in the book.
def count_words(book):

    words = book.split()
    return len(words)

# Receives the book text and returns a dictionary with characters as keys and their frequencies as values.
def count_characters(book):

    characters = {}
    for character in book:
        lowered = character.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

# Generates a formatted report string containing:
# - The total word count
# - Character frequency counts (alphabetical chars only)
# - Sorted in descending order by frequency
def write_report(word_count, chars_dict):

    report = f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n\n"
    char_list = [{"character": char, "char_count": count}
                 for char, count in chars_dict.items()
                 if char.isalpha()]
    char_list.sort(reverse=True, key=lambda dict: dict["char_count"])
    for dictionary in char_list:
        character = dictionary["character"]
        char_count = dictionary["char_count"]
        report += f"The '{character}' character was found {char_count} times\n"
    report += "--- End report ---"
    return report

main()
