

def cap_text(text):
    return text.title()

import unittest

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap_text(text)
        self.assertEqual(result, 'monty Python')

if __name__=='__main__':
    unittest.main()