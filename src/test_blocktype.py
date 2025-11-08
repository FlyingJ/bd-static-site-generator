import unittest

from blocktype import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
	def test_block_to_block_type_0(self):
		block = '# This is a heading'
		result = block_to_block_type(block)
		expectation = BlockType.HEADING
		self.assertEqual(result, expectation)

if __name__ == '__main__':
	unittest.main()