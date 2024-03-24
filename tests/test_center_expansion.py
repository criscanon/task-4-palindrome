import unittest
from algorithms.center_expansion import count_palindromes_center_expansion

class TestCenterExpansionPalindromeCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_palindromes_center_expansion(""), 0)

    def test_single_character(self):
        self.assertEqual(count_palindromes_center_expansion("a"), 1)

    def test_two_identical_characters(self):
        self.assertEqual(count_palindromes_center_expansion("aa"), 3)

    def test_three_characters(self):
        self.assertEqual(count_palindromes_center_expansion("aba"), 4)

    def test_characters_with_different_content(self):
        self.assertEqual(count_palindromes_center_expansion("abcde"), 5)

    def test_characters_with_same_content(self):
        self.assertEqual(count_palindromes_center_expansion("aaaa"), 10)

    def test_even_length_string_no_palindromes(self):
        self.assertEqual(count_palindromes_center_expansion("abcdefg"), 7)

    def test_odd_length_string_no_palindromes(self):
        self.assertEqual(count_palindromes_center_expansion("abcdefgh"), 8)

if __name__ == "__main__":
    unittest.main()
