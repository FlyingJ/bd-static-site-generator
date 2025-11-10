import unittest

from blocktype import BlockType

class TestBlockType(unittest.TestCase):
    def test_blocktype_paragraph(self):
        result = BlockType.PARAGRAPH.value
        expectation = 'paragraph'
        self.assertEqual(result, expectation)

    def test_blocktype_heading(self):
        result = BlockType.HEADING.value
        expectation = 'heading'
        self.assertEqual(result, expectation)

    def test_blocktype_code(self):
        result = BlockType.CODE.value
        expectation = 'code'
        self.assertEqual(result, expectation)

    def test_blocktype_quote(self):
        result = BlockType.QUOTE.value
        expectation = 'quote'
        self.assertEqual(result, expectation)

    def test_blocktype_unordered_list(self):
        result = BlockType.UNORDERED_LIST.value
        expectation = 'unordered_list'
        self.assertEqual(result, expectation)

    def test_blocktype_ordered_list(self):
        result = BlockType.ORDERED_LIST.value
        expectation = 'ordered_list'
        self.assertEqual(result, expectation)

    def test_blocktype_error(self):
        with self.assertRaises(AttributeError):
            result = BlockType.FOO.value

if __name__ == '__main__':
    unittest.main()