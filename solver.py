from nltk.corpus import words
from itertools import product


def get_words(letters, length):
    matching_length_words = set(w for w in words.words() if len(w) == length)
    possible_words = set(
        w for w in matching_length_words if all(l in "".join(letters) for l in w)
    )
    return possible_words


def solver(letters, lengths):
    if not len(letters) == sum(lengths):
        raise Exception(
            "Number of letters must be equal to the total length of all words."
        )
    letters_list = sorted(letters)
    sorted_lengths = sorted(lengths, reverse=True)
    possible_words_dict = dict()
    for i in range(len(lengths)):
        possible_words_dict["word" + str(i)] = get_words(
            letters_list, sorted_lengths[i]
        )
    print(list(product(possible_words_dict.values())))


solver("aeiughkanlkitpfhtesnwie", [1, 4, 4, 9, 5])
