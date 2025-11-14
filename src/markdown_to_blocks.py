def markdown_to_blocks(md):
    new_blocks = []

    remaining = md.strip()
    while remaining != '':
        prior, start_symbol, remaining = remaining.partition('```')
        new_blocks.extend(prior.split('\n\n'))

        if start_symbol == '```' and start_symbol in remaining:
        	code, end_symbol, remaining = remaining.partition('```')
        	new_blocks.append(start_symbol+code+end_symbol)

    return [block for block in new_blocks if block != '']