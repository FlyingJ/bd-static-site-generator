import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_0(self):
        node = HTMLNode(
            'p',
            'this is some text',
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
            )
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_string_repr(self):
        node = HTMLNode(
            'p',
            'this is some text',
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
            )
        print(node)

    def test_props_to_html_1(self):
        node = HTMLNode(
            'a',
            'this is text',
            None,
            {
                "some": "random words",
                "being": "used as properties",
                "href": "https://www.google.com",
                "target": "_blank",
            }
            )
        expected = 'some="random words" being="used as properties" href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()
