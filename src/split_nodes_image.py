import re

from leafnode import LeafNode
from textnode import TextNode
from texttype import TextType

def get_image_boundaries(text):
    # regex for matching image markdown
    regex = r'(!\[([^\]]+)\]\(([^\)]+)\))'
    images = re.finditer(regex, text)
    image_bound_indices = []
    for image in images:
        image_bound_indices.append(image.span())
    return image_bound_indices

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        full_text = old_node.text
        old_texttype = old_node.text_type
        new_texttype = TextType.IMAGE
        
        image_chunks = extract_markdown_images(full_text)
        # we need the start, end indices to cut up some strings
        image_bound_indices = get_image_boundaries(full_text)
        text_chunks = []
        for image_start, image_end in image_bound_indices
        
    return new_nodes
