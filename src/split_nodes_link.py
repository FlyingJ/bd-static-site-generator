from extract_markdown_links import extract_markdown_links
from textnode import TextNode
from texttype import TextType

def split_nodes_link(old_nodes):
    """Accept a list of TextNode objects. Decompose the TextNode objects into
        lists of TextNode text- and link-type objects.

    Args:
        old_nodes(list[TextNode]): the list of TextNode objects to break down

    Returns:
        list[list[TextNode]]: the list of lists of TextNode objects resulting
            from decomposition of the original list of TextNode objects

    """
    # initialize new list for our resulting node lists
    new_nodes = []
    # process old nodes
    for old_node in old_nodes:
        # get the full text from the current old_node
        text = old_node.text
        # get the default text_type for current old_node
        default_text_type = old_node.text_type

        # extract link elements from markdown text node
        # use the link elements to split the text into link and default
        # TextNode objects
        links = extract_markdown_links(text)

        if links is None:
            new_nodes.append(TextNode(text, default_text_type))
            continue

        component_nodes = []

        remaining_text = text
        for link_text, link_url in links:
            leader, remaining_text = remaining_text.split(f'[{link_text}]({link_url})', 1)
            if leader != '':
                component_nodes.append(TextNode(leader, default_text_type))
            component_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        if remaining_text != '':
            component_nodes.append(TextNode(remaining_text, default_text_type))
        
        new_nodes.append(component_nodes)
    # return list of new lists of new TextNode objects
    return new_nodes
