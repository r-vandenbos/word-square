import os
import sys
import time

from joblib.numpy_pickle_utils import xrange


def read_words(square_size, letters):
    my_dir = os.path.dirname(__file__)
    words_file = os.path.join(my_dir, "words.txt")

    # Read and populate list of valid words
    f = open(words_file, "r")
    words_from_file = f.read().split("\n")
    return [w.lower() for w in words_from_file if len(w) == square_size if word_letter_analysis(letters, w)]


def word_letter_analysis(letters, word):
    for letter in word:
        if letter not in letters:
            return False
    return True


def generate_prefixes(words, square_size):
    # Populate Prefixes
    prefixes = {}
    for word in words:
        for i in range(1, square_size):
            if word[:i] in prefixes:
                prefixes[word[:i]].add(word)
            else:
                prefixes[word[:i]] = set()
                prefixes[word[:i]].add(word)

    return prefixes


def print_list():
    for item in sq:
        print(item)
    print("--- %s seconds ---" % (time.time() - start_time))


def engine(sq, prefixes, word_list, depth=0):
    for word_in_list in word_list:
        # # Check if square has been filled or for duplicate word
        if sq[-1] != '':
            return
        else:
            sq[depth] = word_in_list

        if sq[-1] != '':
            return
        else:
            # Get prefix for next recursion
            new_prefix = ""
            for sq_word in sq[:depth + 1]:
                new_prefix += sq_word[depth + 1]

            # Uses prefix to get a list of options
            next_set_of_options = prefixes.get(new_prefix)

            # If options are available then go deeper
            if next_set_of_options:
                engine(sq, prefixes, next_set_of_options, depth + 1)


if __name__ == '__main__':
    start_time = time.time()

    # Get cli params
    square_size = int(sys.argv[1])
    letters = sys.argv[2]

    words = read_words(square_size, letters)

    # Set the square size. I may change this
    sq = ['' for i in xrange(square_size)]

    # Populate Prefixes
    prefixes = generate_prefixes(words, square_size)

    engine(sq, prefixes, words)
    print_list()
