import re

from block_to_blocktype import block_to_blocktype
from blocktype import BlockType
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import textnode_to_htmlnode

MAX_HEADING_LEVEL=6

def process_heading(markdown):
	heading_regex = r'^(#+) (.+)$'
	heading_pattern = re.compile(heading_regex)
	matches = heading_pattern.match(markdown)
	heading_marker = matches.group(1)
	heading_level = min([len(heading_marker), MAX_HEADING_LEVEL])
	heading_text = matches.group(2)
	return heading_level, heading_text

def process_quote_lines(quote_lines):
	children = []
	for quote_line in quote_lines:
		quote_textnodes = text_to_textnodes(quote_line)
		for quote_textnode in quote_textnodes:
			children.append(textnode_to_htmlnode(quote_textnode))
	return children

def process_quote(markdown):
	quote_regex = r'^(> )(.*)$'
	quote_pattern = re.compile(quote_regex)
	dirty_lines = markdown.splitlines()
	clean_lines = []
	for dirty_line in dirty_lines:
		# skip empty lines
		if dirty_line == '':
			continue
		clean_line = quote_pattern.match(dirty_line).group(2)
		clean_lines.append(clean_line)
	blockquote_tag = 'blockquote'
	parent_node = ParentNode(
		tag=blockquote_tag,
		children=process_quote_lines(clean_lines)
	)
	return parent_node

def process_list_item(line):
	return [textnode_to_htmlnode(node) for node in text_to_textnodes(line)]

def process_unordered_list(markdown):
	unordered_list_regex = r'^(- )(.*)$'
	unordered_list_pattern = re.compile(unordered_list_regex)
	dirty_lines = markdown.splitlines()
	children = []
	for dirty_line in dirty_lines:
		if dirty_line == '':
			continue
		clean_line = unordered_list_pattern.match(dirty_line).group(2)
		children.append(
			ParentNode(
				tag='li',
				children=process_list_item(clean_line),
			)
		)
	return children

def process_ordered_list(markdown):
	children = []
	for line in markdown.splitlines():
		if line == '':
			continue
		children.append(
			ParentNode(
				tag='li',
				children=process_list_item(line),
			)
		)
	return children

def process_code(block):
	return block.strip('```').lstrip()

def process_paragraph(block):
	text = ' '.join(block.splitlines())
	return process_list_item(text)

def text_to_children(markdown):
	# convert markdown to blocks
	# identify BlockType
	# if code, skip processing and create <pre><code/></pre> node
	# otherwise, 
	# the children we will return after processing text
	children = []

	child_blocks = markdown_to_blocks(markdown)
	for child_block in child_blocks:
		child_blocktype = block_to_blocktype(child_block)
		match child_blocktype:
			case BlockType.HEADING:
				heading_level, heading_text = process_heading(child_block)
				children.append(
					ParentNode(
						tag=f'h{heading_level}',
						children=process_list_item(heading_text),
					)
				)
				continue
			case BlockType.QUOTE:
				children.append(
					ParentNode(
						tag='blockquote',
						children=[process_quote(child_block)]
					)
				)
				continue
			case BlockType.UNORDERED_LIST:
				children.append(
					ParentNode(
						tag='ul',
						children=process_unordered_list(child_block)
					)
				)
			case BlockType.ORDERED_LIST:
				children.append(
					ParentNode(
						tag='ol',
						children=process_ordered_list(child_block)
					)
				)
			case BlockType.CODE:
				children.append(
					ParentNode(
						tag = 'pre',
						children = [
							LeafNode(
								tag='code',
								value=process_code(child_block)
							),
						],
					)
				)
			case _:
				# if you get here, you are a paragraph
				children.append(
					ParentNode(
						tag = 'p',
						children = process_paragraph(child_block),
					)
				)
	return children

def markdown_to_htmlnode(markdown):
	# primary HTML container is the div
	return ParentNode(
		tag='div',
		children=text_to_children(markdown),
	)