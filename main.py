import sys
from joblib.numpy_pickle_utils import xrange
import time

start_time = time.time()


def word_letter_analysis(letters, word):
    for letter in word:
        if letter not in letters:
            return False
    return True


square_size = int(sys.argv[1])
letters = sys.argv[2]
f = open("words.txt", "r")
words_from_file = f.read().split("\n")
words = [w.lower() for w in words_from_file if len(w) == square_size if word_letter_analysis(letters, w)]

sq = ['' for i in xrange(square_size)]  # Look into better way of doing this.

prefixes = {}

for word in words:
    for i in range(0, square_size):
        # 22 initialises the dict for prefix and stops it from being overwritten.
        prefixes[word[:i]] = prefixes.get(word[:i], set())
        prefixes[word[:i]].add(word)


def engine(w, depth=0):
    for word_in_list in w:
        # Check if square has been filled or for duplicate word
        if sq[-1] or word_in_list in sq:
            break

        sq[depth] = word_in_list

        # Check if square has been filled
        if sq[-1]:
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

# for word1 in words:
#     options1 = prefixes.get(word1[1])
#     sq[0] = word1
#     for word2 in options1:
#         if word2 is word1:
#             break
#         else:
#             sq[1] = word2
#         options2 = prefixes.get(word1[2] + word2[2])
#         if not options2:
#             break
#         for word3 in options2:
#             if word3 in (word1, word2):
#                 break
#             else:
#                 sq[2] = word3
#             options3 = prefixes.get(word1[3] + word2[3] + word3[3])
#             if not options3:
#                 break
#             for word4 in options3:
#                 if word4 in (word1, word2, word3):
#                     break
#                 else:
#                     sq[3] = word4
#
#                     for item in sq:
#                         print(item)
#                     print("------------------")

print("--- %s seconds ---" % (time.time() - start_time))
