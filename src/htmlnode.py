import unittest

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_substrings = []
        for key, value in self.props.items():
            prop_substrings.append(f'{key}="{value}"')
        return ' '.join(prop_substrings)

    def __repr__(self):
        new_string = f'tag: {self.tag}\n'
        new_string += f'value: {self.value}\n'
        new_string += f'children: {self.children}\n'
        new_string += f'props: {self.props}'
        return new_string

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