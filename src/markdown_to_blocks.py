block_delimiter = {
    'code': '```',
    'standard': '\n\n',
}

def markdown_to_blocks(md):
    new_blocks = []
    markdown = md.strip()
    
    if block_delimiter['code'] in markdown:
        # process code, standard mixture
        delimiter = block_delimiter['code']
        search_start = 0
        while delimiter in markdown[search_start:]:
            code_block_start = markdown.index(delimiter, search_start)
            # convert markdown prior to code block
            if code_block_start > search_start:
                new_blocks.extend((markdown[search_start:code_block_start].split(block_delimiter['standard'])))
            search_start = code_block_start + len(delimiter)
            search_start = markdown.index(delimiter, search_start) + len(delimiter)
            new_blocks.append(markdown[code_block_start: search_start])

        new_blocks.extend(markdown[search_start:].split(block_delimiter['standard']))
    else:
        new_blocks.extend(markdown.split(block_delimiter['standard']))
    
    return [block for block in new_blocks if block != '']
