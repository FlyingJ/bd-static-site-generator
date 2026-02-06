def extract_title(markdown):
    '''
    find the line that starts with a single # and return it clean
    '''
    #print('- examining the following markdown')
    #print(markdown)
    #print('- splitting string into lines for processing')
    blocks = [x.strip() for x in markdown.split('\n\n')]
    #print(blocks)
    qualified_blocks = []
    for block in blocks:
        #print(f' - block: {block}')
        if block.startswith('# '):
            #print('-- looks like a title')
            qualified_blocks.append(block)

    if len(qualified_blocks) == 0:
        raise Exception('No title found in markdown')
    elif len(qualified_blocks) > 1:
        raise Exception(f'Too many title lines ({len(qualified_blocks)}) found in markdown')
    else:
        return qualified_blocks[0][1:].strip()