import unittest
from algorithms.dynamic_programming import count_palindromes_dynamic

class TestDynamicProgrammingPalindromeCount(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_palindromes_dynamic(""), 0)

    def test_single_character(self):
        self.assertEqual(count_palindromes_dynamic("a"), 1)

    def test_two_identical_characters(self):
        self.assertEqual(count_palindromes_dynamic("aa"), 3)

    def test_three_characters(self):
        self.assertEqual(count_palindromes_dynamic("aba"), 4)

    def test_characters_with_different_content(self):
        self.assertEqual(count_palindromes_dynamic("abcde"), 5)

    def test_characters_with_same_content(self):
        self.assertEqual(count_palindromes_dynamic("aaaa"), 10)

    def test_even_length_string_no_palindromes(self):
        self.assertEqual(count_palindromes_dynamic("abcdefg"), 7)

    def test_odd_length_string_no_palindromes(self):
        self.assertEqual(count_palindromes_dynamic("abcdefgh"), 8)

if __name__ == "__main__":
    unittest.main()
