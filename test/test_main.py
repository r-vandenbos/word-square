import unittest

from hamcrest import assert_that
from joblib.numpy_pickle_utils import xrange

from main.main import word_letter_analysis, generate_prefixes, read_words, engine


def validate_word_square(sq, sq_size):
    for i in range(0, sq_size):
        w = ""
        for word in sq:
            w += word[i]
        if w != sq[i]:
            return False

    return True


class UserCreationTests(unittest.TestCase):

    @staticmethod
    def test_word_validator():
        assert_that(word_letter_analysis("work", "word") is False, "")
        assert_that(word_letter_analysis("drow", "word") is True, "")

    @staticmethod
    def test_prefix_method():
        prefix_dict = generate_prefixes(["hello"], 5)
        assert_that(len(prefix_dict) == 4, "")

        assert_that("h" in prefix_dict)
        assert_that("hello" in prefix_dict["h"])
        assert_that("he" in prefix_dict)
        assert_that("hello" in prefix_dict["he"])
        assert_that("hel" in prefix_dict)
        assert_that("hello" in prefix_dict["hel"])
        assert_that("hell" in prefix_dict)
        assert_that("hello" in prefix_dict["hell"])

    @staticmethod
    def test_read_words():
        words = read_words(4, "eeeeddoonnnsssrv")
        assert_that(len(words) == 86)

        assert_that(len([word for word in words if len(word) != 4]) == 0)

    @staticmethod
    def test_four_word_square():
        sq_size = 4

        words = read_words(sq_size, "aaccdeeeemmnnnoo")

        sq = ['' for i in xrange(sq_size)]

        # Populate Prefixes
        prefixes = generate_prefixes(words, sq_size)

        engine(sq, prefixes, words)

        assert_that(validate_word_square(sq, sq_size), "")

    @staticmethod
    def test_five_word_square():
        sq_size = 5
        words = read_words(sq_size, "aaaeeeefhhmoonssrrrrttttw")

        sq = ['' for i in xrange(sq_size)]

        # Populate Prefixes
        prefixes = generate_prefixes(words, sq_size)

        engine(sq, prefixes, words)

        assert_that(validate_word_square(sq, sq_size), "")

    @staticmethod
    def test_seven_word_square():
        sq_size = 7
        words = read_words(sq_size, "aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy")

        sq = ['' for i in xrange(sq_size)]

        # Populate Prefixes
        prefixes = generate_prefixes(words, sq_size)

        engine(sq, prefixes, words)

        assert_that(validate_word_square(sq, sq_size), "")

    @staticmethod
    def test_validator_method():
        valid_word_square = ['acme', 'coed', 'mead', 'eddo']
        assert_that(validate_word_square(valid_word_square, 4), "")

        invalid_word_square = ['acme', 'blah', 'mead', 'eddo']
        assert_that(validate_word_square(invalid_word_square, 4) is False, "")


if __name__ == '__main__':
    unittest.main()
