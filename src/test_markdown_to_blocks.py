import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
	def test_markdown_to_blocks_0(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
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
			'```\n#include <stdio.h>\n\nint main()\n{\n\tprintf("Hello, World!\\n");\n\treturn 0;\n}\n```'
		]
		self.assertEqual(result, expectation)

if __name__ == '__main__':
	unittest.main()