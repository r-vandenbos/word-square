import sys
import time

from joblib.numpy_pickle_utils import xrange

start_time = time.time()


def word_letter_analysis(letters, word):
    for letter in word:
        if letter not in letters:
            return False
    return True


# Get cli params
square_size = int(sys.argv[1])
letters = sys.argv[2]

# Read and populate list of valid words
f = open("words.txt", "r")
words_from_file = f.read().split("\n")
words = [w.lower() for w in words_from_file if len(w) == square_size if word_letter_analysis(letters, w)]

# Set the square size. I may change this
sq = ['' for i in xrange(square_size)]

# Populate Prefixes
prefixes = {}
for word in words:
    for i in range(1, square_size):
        if word[:i] in prefixes:
            prefixes[word[:i]].add(word)
        else:
            prefixes[word[:i]] = set()
            prefixes[word[:i]].add(word)


def engine(w, depth=0):
    for word_in_list in w:
        # # Check if square has been filled or for duplicate word
        if sq[-1] != '' or word_in_list in sq:
            break

        sq[depth] = word_in_list

        if sq[-1] != '':
            break

        # Get prefix for next recursion
        new_prefix = ""
        for sq_word in sq[:depth + 1]:
            new_prefix += (sq_word[depth + 1])

        # Uses prefix to get a list of options
        next_set_of_options = prefixes.get(new_prefix)

        # If options are available then go deeper
        if next_set_of_options:
            engine(next_set_of_options, depth + 1)


engine(words)

for item in sq:
    print(item)
print("--- %s seconds ---" % (time.time() - start_time))
