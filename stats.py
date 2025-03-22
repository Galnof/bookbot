# Receives the book text and counts the amount of words in the book.
def count_words(book):

    words = book.split()
    return len(words)

# Receives the book text and returns a dictionary with
# characters as keys and their frequencies as values.
def count_characters(book):

    characters = {}
    for character in book:
        lowered = character.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

# Receives a dictionary of character counts
# and returns a list of character count dictionaries
# that are sorted in descending order by frequency.
def chars_dict_to_sorted_list(chars_dict):
    chars_list = [{"character": char, "char_count": count}
                 for char, count in chars_dict.items()
                 if char.isalpha()]
    chars_list.sort(reverse=True, key=lambda dict: dict["char_count"])
    return chars_list
