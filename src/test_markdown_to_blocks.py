import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_0(self):
        md = '''
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
'''
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_1(self):
        md = '''
## Some code

```
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
}
```
'''
        result = markdown_to_blocks(md)
        expectation = [
            '## Some code',
            '```\n#include <stdio.h>\n\nint main()\n{\n    printf("Hello, World!\n");\n    return 0;\n}\n```'
        ]
        self.assertEqual(result, expectation)

    def test_markdown_to_blocks_2(self):
        md = '''
# This **is** a _heading_

There is some regular text going on here
now and there will be _italics_ and **bold**
stuff.

## There will be exposition and quotes

There will be gobbldy gook written that will pass down the
ages, improving the lot of no one. Not once. Not ever.

So sayeth:

> That shit _Jay_ said?
> That was some **bullshit**.
> Maddening, it is.

## There will be lists

- An **unordered** list item
- _Another_ unordered list item

## There may be numbered lists

1. Item 1
2. **Item** 2
3. Item **3**
4. Item 4

## Some code

```
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
}
```

And a final plain, text paragraph.

'''
        result = markdown_to_blocks(md)
        expectation = [
            '# This **is** a _heading_',
            'There is some regular text going on here\nnow and there will be _italics_ and **bold**\nstuff.',
            '## There will be exposition and quotes',
            'There will be gobbldy gook written that will pass down the\nages, improving the lot of no one. Not once. Not ever.',
            'So sayeth:',
            '> That shit _Jay_ said?\n> That was some **bullshit**.\n> Maddening, it is.',
            '## There will be lists',
            '- An **unordered** list item\n- _Another_ unordered list item',
            '## There may be numbered lists',
            '1. Item 1\n2. **Item** 2\n3. Item **3**\n4. Item 4',
            '## Some code',
            '```\n#include <stdio.h>\n\nint main()\n{\n    printf("Hello, World!\n");\n    return 0;\n}\n```',
            'And a final plain, text paragraph.'
        ]
        self.assertEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()
