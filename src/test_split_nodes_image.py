import unittest

from split_nodes_image import split_nodes_image
from textnode import TextNode
from texttype import TextType

class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_0(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expectation = [[
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ]]
        self.assertListEqual(result, expectation)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is only text!", TextType.TEXT)
        result = split_nodes_image([node])
        expectation = [[TextNode("This is only text!", TextType.TEXT)]]
        self.assertEqual(result, expectation)

    def test_split_nodes_image_only_images(self):
        node = TextNode(
            "![some fake image](https://secure.example.com/fake.jpeg)![another fake image](http://pic.com/something.gif)![foo](http://foo.com/foo.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        expectation = [[
            TextNode("some fake image", TextType.IMAGE, "https://secure.example.com/fake.jpeg"),
            TextNode("another fake image", TextType.IMAGE, "http://pic.com/something.gif"),
            TextNode("foo", TextType.IMAGE, "http://foo.com/foo.png")
        ]]
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()