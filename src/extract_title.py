def extract_title(markdown):
    '''
    find the line that starts with a single # and return it clean
    '''
    #print('- examining the following markdown')
    #print(markdown)
    #print('- splitting string into lines for processing')
    blocks = [x.strip() for x in markdown.split('\n\n')]
    #print(blocks)
    qualified_lines = []
    for block in blocks:
        lines = block.split('\n')
        #print(f' - block: {block}')
        for line in lines:
            if line.startswith('# '):
                #print('-- looks like a title')
                qualified_lines.append(line)

    qualifier_count = len(qualified_lines)
    if qualifier_count == 0:
        raise Exception('No title found in markdown')
    elif qualifier_count > 1:
        raise Exception(f'Too many title lines ({qualifier_count}) found in markdown')
    else:
        return qualified_lines[0][1:].strip()