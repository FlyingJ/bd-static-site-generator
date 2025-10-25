import unittest

from leafnode import LeafNode
from parentnode import ParentNode

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