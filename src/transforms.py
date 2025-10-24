import unittest

import re

from leafnode import LeafNode
from textnode import TextNode
from texttype import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    new_type = text_type    

    for old_node in old_nodes:
        more_newer_nodes = []
        old_text = old_node.text
        old_type = old_node.text_type
        
        substrings = old_text.split(delimiter)
        do_new_type = False
        for substring in substrings:
            more_newer_nodes.append(TextNode(substring, new_type if do_new_type else old_type))
            do_new_type = not do_new_type
        new_nodes.append(more_newer_nodes)
    return new_nodes

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

def text_node_to_html_node(text_node):
    conversion_map = {
        'text': lambda x: LeafNode(None,x.text),
        'bold': lambda x: LeafNode("b", x.text),
        'italic': lambda x: LeafNode("i", x.text),
        'code': lambda x: LeafNode("code", x.text),
        'link': lambda x: LeafNode("a", x.text, {"href": x.url}),
        'image': lambda x: LeafNode("img", "", {"src": x.url, "alt": x.text}),
    }
    return conversion_map[text_node.text_type.value](text_node)

class TestTextToHTML(unittest.TestCase):
    def test_text_to_html_node_text_0(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_to_html_node_text_1(self):
        text_node = TextNode('this is some text', TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        result = html_node.to_html()
        expectation = 'this is some text'
        self.assertEqual(result, expectation)

    def test_text_to_html_node_bold(self):
        text_node = TextNode('this is some bold text', TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        result = html_node.to_html()
        expectation = '<b>this is some bold text</b>'
        self.assertEqual(result, expectation)

    def test_text_to_html_node_italic(self):
        text_node = TextNode('this is some italic text', TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        result = html_node.to_html()
        expectation = '<i>this is some italic text</i>'
        self.assertEqual(result, expectation)

    def test_text_to_html_node_code(self):
        text_node = TextNode('this is some code', TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        result = html_node.to_html()
        expectation = '<code>this is some code</code>'
        self.assertEqual(result, expectation)

    def test_text_to_html_node_link(self):
        text_node = TextNode("click here", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(text_node)
        result = html_node.to_html()
        expectation = '<a href="http://example.com">click here</a>'
        self.assertEqual(result, expectation)

    def test_text_to_html_node_image(self):
        text_node = TextNode("this is alternate text", TextType.IMAGE, "http://example.com/picture.png")
        html_node = text_node_to_html_node(text_node)
        result = html_node.to_html()
        expectation = '<img src="http://example.com/picture.png" alt="this is alternate text"></img>'
        self.assertEqual(result, expectation)

    def test_text_to_html_node_error(self):
        pass

if __name__ == '__main__':
    unittest.main()
