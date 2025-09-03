import unittest
from task_3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("Madam"))

    def test_sentence_palindrome(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_sentence_palindrome("Hello, world!"))

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))

    def test_spaces_and_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))

    def test_mixed_case(self):
        self.assertTrue(is_sentence_palindrome("No 'x' in Nixon"))

    def test_numbers(self):
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertFalse(is_sentence_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()

    # Take input from the user and check if it's a sentence palindrome
    user_input = input("Enter a sentence to check if it's a palindrome: ")
    if is_sentence_palindrome(user_input):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")