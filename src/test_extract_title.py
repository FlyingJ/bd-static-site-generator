import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_0(self):
        markdown = '''# This is the Title

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque suscipit mauris accumsan, accumsan tortor sit amet, mollis quam.
Vestibulum feugiat ante id ligula ornare, placerat imperdiet felis commodo.
Nulla ut dui fringilla, facilisis orci varius, porttitor ex.
'''
        result = extract_title(markdown)
        expectation = 'This is the Title'
        self.assertEqual(result, expectation)

    def test_1(self):
        markdown = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque suscipit mauris accumsan, accumsan tortor sit amet, mollis quam.
Vestibulum feugiat ante id ligula ornare, placerat imperdiet felis commodo.
Nulla ut dui fringilla, facilisis orci varius, porttitor ex.

Ut varius neque vitae felis consectetur aliquam.
Aenean et eros cursus, condimentum magna eu, pulvinar augue.
Phasellus vitae augue a sem condimentum ullamcorper.
Fusce id quam eu turpis rutrum pulvinar quis et erat.
Duis pellentesque odio id neque mattis tempor ac at ante.

Aliquam luctus purus a ex accumsan facilisis.
Morbi sed libero ut nibh scelerisque dignissim nec ut nibh.
Donec imperdiet justo nec sem rhoncus varius.

Donec ut sem ut justo fringilla eleifend.
Vivamus sed lacus eget diam feugiat pharetra eget quis mauris.
Praesent vitae risus id arcu cursus mattis sed a orci.

Sed condimentum ex eu porta suscipit.
Donec commodo ipsum ac leo laoreet aliquam.'''
        with self.assertRaises(Exception):
            result = extract_title(markdown)

    def test_2(self):
        markdown = '''# This is the Title

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque suscipit mauris accumsan, accumsan tortor sit amet, mollis quam.

Vestibulum feugiat ante id ligula ornare, placerat imperdiet felis commodo.
Nulla ut dui fringilla, facilisis orci varius, porttitor ex.

# Another Title Line'''
        with self.assertRaises(Exception):
            result = extract_title(markdown)

    def test_3(self):
        markdown = '''# This is the Title
# This second line is an edge case

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Quisque suscipit mauris accumsan, accumsan tortor sit amet, mollis quam.

Vestibulum feugiat ante id ligula ornare, placerat imperdiet felis commodo.
Nulla ut dui fringilla, facilisis orci varius, porttitor ex.'''
        with self.assertRaises(Exception):
            result = extract_title(markdown)

if __name__ == "__main__":
    unittest.main()