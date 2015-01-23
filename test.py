__author__ = 'parknature'

import hangmantest
import unittest

class hangmanTestCase(unittest.TestCase):
    def test_checkCorrectAnswer(self):
        ret = hangmantest.checkCorrectAnswer('tac', 'cat')
        self.assertTrue(ret)

    def test_checkWrongAnswer(self):
        ret = hangmantest.checkCorrectAnswer('ta', 'cat')
        self.assertEqual(ret, False)


if __name__ == "__main__":
    unittest.main()