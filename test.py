__author__ = 'parknature'

import hangman
import unittest

class hangmanTestCase(unittest.TestCase):
    def test_checkCorrectAnswer(self):
        ret = hangman.checkCorrectAnswer('tac', 'cat')
        self.assertTrue(ret)

    def test_checkWrongAnswer(self):
        ret = hangman.checkCorrectAnswer('ta', 'cat')
        self.assertEqual(ret, False)


if __name__ == "__main__":
    unittest.main()
