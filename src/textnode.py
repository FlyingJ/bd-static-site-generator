import unittest

from texttype import TextType

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        if (
            self.text == target.text and
            self.text_type.value == target.text_type.value and
            self.url == target.url
            ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

class TestTextNode(unittest.TestCase):
    def test_eq_0(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_1(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_0(self):
        node = TextNode("Some text", TextType.TEXT)
        node2 = TextNode("Some text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_1(self):
        node = TextNode("A text", TextType.TEXT)
        node2 = TextNode("Another text", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    unittest.main()