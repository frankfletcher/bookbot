from collections import Counter


def get_num_words(text: str) -> int:
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())


def count_chars(text: str) -> int:
    return dict(Counter(text.lower()))


def get_sorted_list_char_counts(char_counts: dict):
    cc_list = []

    cc_list.extend({"char": k, "num": v} for k, v in char_counts.items())

    cc_list.sort(reverse=True, key=lambda x: x["num"])

    return cc_list
