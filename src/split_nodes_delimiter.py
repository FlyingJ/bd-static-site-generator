from textnode import TextNode
from texttype import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    new_type = text_type    

    for old_node in old_nodes:
        # TextNode objects of image, link types pass through
        if old_node.text_type in [TextType.IMAGE, TextType.LINK]:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        old_type = old_node.text_type
        
        substrings = text.split(delimiter)
        if len(substrings)%2 != 1:
            raise Exception(f'- mismatched delimiter: {delimiter}')
        do_new_type = False
        for substring in substrings:
            new_nodes.append(TextNode(substring, new_type if do_new_type else old_type))
            do_new_type = not do_new_type

    return new_nodes