from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_heading(block):
    return True if block.startswith(('# ','## ', '### ', '#### ', '##### ', '###### ')) else False

def is_code(block):
    return True if (block.startswith('```') and block.endswith('```')) else False

def is_quote(block):
    for line in block.splitlines():
        if not line.startswith('> '):
            return False
    return True

def is_unordered_list(block):
    for line in block.splitlines():
        if not line.startswith('- '):
            return False
    return True

def is_ordered_list(block):
    for index, line in enumerate(block.splitlines()):
        if not line.startswith(str(index+1)+'. '):
            return False
    return True

def block_to_block_type(markdown):
    # is it a heading?
    if is_heading(markdown):
        return BlockType.HEADING
    # is it a code block?
    if is_code(markdown):
        return BlockType.CODE
    # perhaps a quote
    if is_quote(markdown):
        return BlockType.QUOTE
    # or an unordered list
    if is_unordered_list(markdown):
        return BlockType.UNORDERED_LIST
    # but the list may be ordered as well
    if is_ordered_list(markdown):
        return BlockType.ORDERED_LIST
    # if we make it here, the block must be plain text
    return BlockType.PARAGRAPH