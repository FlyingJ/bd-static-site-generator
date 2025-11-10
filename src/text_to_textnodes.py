from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode
from texttype import TextType

def text_to_textnodes(text):
	text_node = TextNode(text, TextType.TEXT)
	# TEXT = "text"
	# BOLD = "bold"
	# ITALIC = "italic"
	# CODE = "code"
	# LINK = "link"
	# IMAGE = "image"

	# we have a full string of markdown text
	# we have a TextNode made from said text
	# start building out node list by splitting out images and links
	new_nodes = split_nodes_image([text_node])
	new_nodes = split_nodes_link(new_nodes)
	new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
	new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
	new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

	return new_nodes