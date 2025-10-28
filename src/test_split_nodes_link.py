import unittest

from split_nodes_link import split_nodes_link
from textnode import TextNode
from texttype import TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_0(self):
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

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is only text!", TextType.TEXT)
        result = split_nodes_link([node])
        expectation = [TextNode("This is only text!", TextType.TEXT)]
        self.assertEqual(result, expectation)

    def test_split_nodes_link_only_links(self):
        node = TextNode(
            "[some fake link](https://secure.example.com/fake.html)[another fake link](http://pic.com/something.gif)[foo](http://foo.com/foo.tgz)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        expectation = [
            TextNode("some fake link", TextType.LINK, "https://secure.example.com/fake.html"),
            TextNode("another fake link", TextType.LINK, "http://pic.com/something.gif"),
            TextNode("foo", TextType.LINK, "http://foo.com/foo.tgz")
        ]
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()