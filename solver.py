from nltk.corpus import words
import itertools


def get_words(letters, length):
    matching_length_words = set(w for w in words.words() if len(w) == length)
    possible_words = set(w for w in matching_length_words if all(l in "".join(letters) for l in w))
    return possible_words

print(get_words(["h", "o", "r", "s", "t"], 5))