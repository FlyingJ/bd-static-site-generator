from textnode import TextNode
from texttype import TextType

# DEFAULT_TEXTTYPE = TextType.TEXT

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    new_type = text_type    

    for old_node in old_nodes:
        text = old_node.text
        old_type = old_node.text_type
        
        # TextNode objects of image, link types pass through
        # as do TextNode objects whose text does not contain
        # the current delimiter
        if (old_node.text_type in [TextType.IMAGE, TextType.LINK]):
            new_nodes.append(old_node)
            continue
        if (delimiter not in old_node.text):
            new_nodes.append(old_node)
            continue

        current_type = old_type

        splits = text.split(delimiter)

        for split in splits:
            new_nodes.append(
                TextNode(
                    text=split,
                    text_type=current_type
                )
            )
            current_type = new_type if current_type == old_type else old_type

    return new_nodes