import unittest

from blocktype import BlockType, block_to_block_type

block_to_block_type_test_cases = [
	('# This is a Heading 1 block', BlockType.HEADING),
	('## This is a Heading 2 block', BlockType.HEADING),
	('### This is a Heading 3 block', BlockType.HEADING),
	('#### This is a Heading 4 block', BlockType.HEADING),
	('##### This is a Heading 5 block', BlockType.HEADING),
	('###### This is a Heading 6 block', BlockType.HEADING),
	('```This is a simple Code block```', BlockType.CODE),
	('> fdsafdsfdsafds\n> fdafdafds\n> fdafdsafdsfdsafd', BlockType.QUOTE),
	('- item\n- another item\n- more other item\n- more item', BlockType.UNORDERED_LIST),
	('1. item 1\n2. item 2\n3. item 3\n4. item 4', BlockType.ORDERED_LIST),
	('this is some basic text', BlockType.PARAGRAPH),
	(' ```This is a simple Code block```', BlockType.PARAGRAPH),
	('>fdsafdsfdsafds\n> fdafdafds\n> fdafdsafdsfdsafd', BlockType.PARAGRAPH),
	('- item\n- another item\n-more other item\n- more item', BlockType.PARAGRAPH),
	('1. item 1\n5. item 2\n3. item 3\n4. item 4', BlockType.PARAGRAPH),	
]

class TestBlockToBlockType(unittest.TestCase):
	def test_block_to_block_type_0(self):
		for block, expectation in block_to_block_type_test_cases: 
			result = block_to_block_type(block)
			self.assertEqual(result, expectation)

if __name__ == '__main__':
	unittest.main()