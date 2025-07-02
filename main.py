from stats import get_num_words, count_chars, get_sorted_list_char_counts
import sys


def get_book_text(filepath: str) -> str:
    """
    Reads the content of a book file and returns it as a string.

    Args:
        filepath (str): The path to the book file.

    Returns:
        str: The content of the book.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    """
    Main function to execute the script.
    """
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1] 
    
    book_text = get_book_text(filepath)
    # print(book_text)
    num_words = get_num_words(book_text)
    # print(f"{num_words} words found in the document")

    char_counts = count_chars(book_text)
    # print(f"Char Counts: {char_counts}")

    cc_list = get_sorted_list_char_counts(char_counts)

    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")

    for char_dict in cc_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")

    print("============= END ===============")


main()
