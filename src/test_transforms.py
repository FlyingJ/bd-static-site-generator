import unittest

from leafnode import LeafNode
from transforms import split_nodes_delimiter
from textnode import TextNode
from texttype import TextType

class TestTextSplitDelimiterTransforms(unittest.TestCase):
    def test_split_nodes_delimiter_text_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expectation = [
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        ]
        self.assertEqual(result, expectation)

    def test_split_nodes_delimiter_text_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expectation = [
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
        ]
        self.assertEqual(result, expectation)

    def test_split_nodes_delimiter_text_italic(self):
        node = TextNode("This is text with an _italicized_ word", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expectation = [
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
        ]
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()