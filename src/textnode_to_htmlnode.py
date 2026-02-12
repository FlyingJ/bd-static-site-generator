from leafnode import LeafNode

def textnode_to_htmlnode(text_node):
    conversion_map = {
        'text': lambda x: LeafNode(None, x.text),
        'bold': lambda x: LeafNode("b", x.text),
        'italic': lambda x: LeafNode("i", x.text),
        'code': lambda x: LeafNode("code", x.text),
        'link': lambda x: LeafNode("a", x.text, {"href": x.url}),
        'image': lambda x: LeafNode("img", "", {"src": x.url, "alt": x.text}),
    }
    return conversion_map[text_node.text_type.value](text_node)
