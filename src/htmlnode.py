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
