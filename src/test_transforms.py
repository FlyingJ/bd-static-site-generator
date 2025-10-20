import unittest

from textnode import TextNode
from texttype import TextType
from transforms import split_nodes_delimiter
from transforms import extract_markdown_links
from transforms import split_nodes_link
from transforms import extract_markdown_images
from transforms import split_nodes_image
from transforms import text_node_to_html_node

class TestTextToHTMLTransforms(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_to_html_node_text(self):
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

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links_0(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expectation = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(result, expectation)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_0(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expectation = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(result, expectation)

    def test_extract_markdown_images_1(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        result = extract_markdown_images(text)
        expectation = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertEqual(result, expectation)
        
class TestTextSplitImageTransforms(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expectation = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ]
        self.assertListEqual(result, expectation)
    
class TestTextSplitLinkTransforms(unittest.TestCase):
    def test_split_links_0(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        expectation = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()
