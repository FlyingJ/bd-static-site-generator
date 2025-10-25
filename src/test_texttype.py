import unittest

from texttype import TextType

class TestTextType(unittest.TestCase):
    def test_texttype_text(self):
        result = TextType.TEXT.value
        expectation = 'text'
        self.assertEqual(result, expectation)

    def test_texttype_bold(self):
        result = TextType.BOLD.value
        expectation = 'bold'
        self.assertEqual(result, expectation)

    def test_texttype_italic(self):
        result = TextType.ITALIC.value
        expectation = 'italic'
        self.assertEqual(result, expectation)

    def test_texttype_code(self):
        result = TextType.CODE.value
        expectation = 'code'
        self.assertEqual(result, expectation)

    def test_texttype_link(self):
        result = TextType.LINK.value
        expectation = 'link'
        self.assertEqual(result, expectation)

    def test_texttype_image(self):
        result = TextType.IMAGE.value
        expectation = 'image'
        self.assertEqual(result, expectation)

    def test_texttype_error(self):
        with self.assertRaises(AttributeError):
            result = TextType.FOO.value

if __name__ == '__main__':
    unittest.main()