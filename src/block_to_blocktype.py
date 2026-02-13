from blocktype import BlockType

def is_heading(block):
    return True if block.startswith(('# ','## ', '### ', '#### ', '##### ', '###### ')) else False

def is_code(block):
    return True if (block.startswith('```') and block.endswith('```')) else False

def is_quote(block):
    for line in block.splitlines():
        if not line.startswith('>'):
            return False
    # print(f' - is_quote: identified blockquote')
    # print(block)
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

def block_to_blocktype(markdown):
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
    