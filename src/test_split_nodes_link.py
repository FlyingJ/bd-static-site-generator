import unittest

from split_nodes_link import get_bounds
from split_nodes_link import split_nodes_link
from textnode import TextNode
from texttype import TextType

class TestGetBounds(unittest.TestCase):
    def test_get_bounds_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link_locater = get_bounds(TextType.LINK)
        result = link_locater(text)
        expectation = [(24, 60), (64, 114)]
        self.assertEqual(result, expectation)

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links_0(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT)
        result = split_nodes_link([node])
        print(result)
        expectation = [[
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]]
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()