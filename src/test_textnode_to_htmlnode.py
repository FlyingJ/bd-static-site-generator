import unittest

from textnode_to_htmlnode import textnode_to_htmlnode
from textnode import TextNode
from texttype import TextType

class TestTextToHTML(unittest.TestCase):
    def test_textnode_to_htmlnode_text_0(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_textnode_to_htmlnode_text_1(self):
        text_node = TextNode('this is some text', TextType.TEXT)
        html_node = textnode_to_htmlnode(text_node)
        result = html_node.to_html()
        expectation = 'this is some text'
        self.assertEqual(result, expectation)

    def test_textnode_to_htmlnode_bold(self):
        text_node = TextNode('this is some bold text', TextType.BOLD)
        html_node = textnode_to_htmlnode(text_node)
        result = html_node.to_html()
        expectation = '<b>this is some bold text</b>'
        self.assertEqual(result, expectation)

    def test_textnode_to_htmlnode_italic(self):
        text_node = TextNode('this is some italic text', TextType.ITALIC)
        html_node = textnode_to_htmlnode(text_node)
        result = html_node.to_html()
        expectation = '<i>this is some italic text</i>'
        self.assertEqual(result, expectation)

    def test_textnode_to_htmlnode_code(self):
        text_node = TextNode('this is some code', TextType.CODE)
        html_node = textnode_to_htmlnode(text_node)
        result = html_node.to_html()
        expectation = '<code>this is some code</code>'
        self.assertEqual(result, expectation)

    def test_textnode_to_htmlnode_link(self):
        text_node = TextNode("click here", TextType.LINK, "http://example.com")
        html_node = textnode_to_htmlnode(text_node)
        result = html_node.to_html()
        expectation = '<a href="http://example.com">click here</a>'
        self.assertEqual(result, expectation)

    def test_textnode_to_htmlnode_image(self):
        text_node = TextNode("this is alternate text", TextType.IMAGE, "http://example.com/picture.png")
        html_node = textnode_to_htmlnode(text_node)
        result = html_node.to_html()
        expectation = '<img src="http://example.com/picture.png" alt="this is alternate text"></img>'
        self.assertEqual(result, expectation)

    def test_textnode_to_htmlnode_error(self):
        pass

if __name__ == '__main__':
    unittest.main()