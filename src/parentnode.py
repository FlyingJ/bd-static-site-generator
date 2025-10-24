import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('tag cannot be None')
        if self.value is not None:
            raise ValueError('value must be None')
        if self.children is None:
            raise ValueError('ParentNode children must not be None')
        html_string = ''
        html_string += f'<{self.tag}'
        if self.props:
            html_string += f' {self.props_to_html()}'
        html_string += '>'
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string

class TestParentNode(unittest.TestCase):

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        
        result = parent_node.to_html()
        expectation = '<div><span>child</span></div>'
        self.assertEqual(result, expectation)

    def test_to_html_with_children(self):
        node = ParentNode(
            'p',
            [
                LeafNode('b', 'Bold text'),
                LeafNode(None, 'Normal text'),
                LeafNode('i', 'italic text'),
                LeafNode(None, 'Normal text'),
            ],
        )
        
        result = node.to_html()
        expectation = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(result, expectation)
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        
        result = parent_node.to_html()
        expectation = '<div><span><b>grandchild</b></span></div>'
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()
