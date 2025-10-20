from leafnode import LeafNode
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    new_type = text_type    

    for old_node in old_nodes:
        more_newer_nodes = []
        old_text = old_node.text
        old_type = old_node.text_type
        
        substrings = old_text.split(delimiter)
        do_new_type = False
        for substring in substrings:
            more_newer_nodes.append(TextNode(substring, new_type if do_new_type else old_type))
            do_new_type = not do_new_type
        new_nodes.append(more_newer_nodes)
    return new_nodes

def text_node_to_html_node(text_node):
    conversion_map = {
        'text': lambda x: LeafNode(None,x.text),
        'bold': lambda x: LeafNode("b", x.text),
        'italic': lambda x: LeafNode("i", x.text),
        'code': lambda x: LeafNode("code", x.text),
        'link': lambda x: LeafNode("a", x.text, {"href": x.url}),
        'image': lambda x: LeafNode("img", "", {"src": x.url, "alt": x.text}),
    }
    return conversion_map[text_node.text_type.value](text_node)
