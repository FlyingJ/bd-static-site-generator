import unittest

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag is None:
            return self.value
        html_string = ""
        html_string += f"<{self.tag}"
        if self.props:
            html_string += f" {self.props_to_html()}"
        html_string += f">{self.value}</{self.tag}>"
        return html_string

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p_0(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
     
    def test_leaf_to_html_p_1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_to_html_value_error(self):
        faulty_leafnode = LeafNode()
        self.assertRaises(ValueError, faulty_leafnode.to_html)

if __name__ == "__main__":
    unittest.main()
