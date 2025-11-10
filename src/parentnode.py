from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(
            tag=tag,
            value=None,
            children=children,
            props=props
        )

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
