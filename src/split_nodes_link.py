import re

from extract_markdown_links import extract_markdown_links
from textnode import TextNode
from texttype import TextType

markdown_regexes = {
    'image': r'(!\[([^\]]+)\]\(([^\)]+)\))',
    'link': r'([^!]\[([^\]]+)\]\(([^\)]+)\))',
}

def get_bounds(text_type):
    """Accept a TextType and return a function which locates start, end indices
    of substrings matching the value of the TextType object.

    Args:
        text_type (TextType): The type of text to search for, e.g., link, image
        
    Returns:
        function: Locater function for substrings of matching text type
    """
    regex = markdown_regexes[text_type.value]
    def locater(text):
        """Locates start, end indices of substrings matching regex.

        Args:
            text (str): The text string to search

        Returns:
            list[(int, int)]: The list of (start, end) indices of substrings
                matching regex
        """
        substrings = re.finditer(regex, text)
        bounds = []
        for substring in substrings:
            bounds.append(substring.span())
        return bounds
    return locater

def get_link_nodes(text):
    new_nodes = []
    # create link substring locater function
    get_link_bounds = get_bounds(TextType.LINK)
    link_bounds = get_link_bounds(text)
    link_components = extract_markdown_links(text)
    for text, url in link_components:
        new_nodes.append(
            (link_bounds.pop(0), TextNode(text, TextType.LINK, url))
        )
    return new_nodes

def split_nodes_link(old_nodes):
    """Accept a list of TextNode objects. Decompose the TextNode objects into
        lists of LeafNode text- and link-type objects.

    Args:
        old_nodes(list[TextNode]): the list of TextNode objects to break down

    Returns:
        list[list[LeafNode]]: the list of lists of LeafNode objects resulting
            from decomposition of the original list of TextNode objects

    """
    # initialize new list for our resulting node lists
    new_nodes = []
    # process old nodes
    for old_node in old_nodes:
        # get the full text from the current old_node
        full_text = old_node.text
        # get the default text_type for current old_node
        default_text_type = old_node.text_type

        # extract the text nodes for links
        link_nodes = get_link_nodes(full_text)
        # still need text nodes for the non-link segments
        nonlink_nodes = get_nonlink_nodes(link_nodes, default_text_type)

    # return list of new lists of new leaf nodes
    return new_nodes