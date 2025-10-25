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
