"""Debugger exercise."""


from contextlib import nullcontext
from venv import create


def split_string(string):
    """Given a string, split it into a list of 'words'."""
    start_of_word = 0
    words = []
    for i in range(len(string)):
        if string[i] == " ":
            words.append(string[start_of_word:i])
            start_of_word = i
    return words


def count_words(words):
    """Count how often words occur in a list."""
    word_counts = dict()
    for i in words:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1
    return word_counts


def create_collective_count(word_counts1, word_counts2):
    """Take two word counters and combine them into one."""
    collective_count = dict()
    for i in word_counts1:
        if i in word_counts2:
            collective_count[i] = word_counts1[i] + word_counts2[i]
    return collective_count


def word_counter(string1: str, string2: str) -> str:
    """Find the word that occurs the most across the two strings."""
    string1_words = split_string(string1)
    string2_words = split_string(string2)
    word_counts1 = count_words(string1_words)
    word_counts2 = count_words(string2_words)
    collective_count = create_collective_count(word_counts1, word_counts2)
    curr_max = 0
    for i in collective_count:
        if collective_count[i] > curr_max:
            curr_max = collective_count[i]
            curr_word = i
    return curr_word


if __name__ == "__main__":
    # Test Case 1, No Overlapping Words
    string1 = "I love Practical Data Science."
    string2 = "Who is Nick Eubank?"
    test_word = word_counter(string1, string2)
    # Test Case 2, 'code'
    string1 = "This is a test of my code."
    string2 = "I hope there's not bugs in this code."
    test_word = word_counter(string1, string2)
