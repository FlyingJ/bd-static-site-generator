import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            'p',
            'this is some text',
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
            )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)        
    
    def test_eq_1(self):
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
        pass

if __name__ == "__main__":
    unittest.main()