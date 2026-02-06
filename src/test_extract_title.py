import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_0(self):
        markdown = '''
# This is the Title

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque suscipit mauris accumsan, accumsan tortor sit amet, mollis quam.
Vestibulum feugiat ante id ligula ornare, placerat imperdiet felis commodo.
Nulla ut dui fringilla, facilisis orci varius, porttitor ex.
'''
        result = extract_title(markdown)
        expectation = 'This is the Title'
        self.assertEqual(result, expectation)


if __name__ == "__main__":
    unittest.main()