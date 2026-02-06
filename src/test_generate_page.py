import unittest

from generate_page import generate_page

class TestGeneratePage(unittest.TestCase):
    def test_0(self):
        from_path = ''
        template_path = ''
        dest_path = ''
        with self.assertRaises(Exception):
            generate_page(from_path, template_path, dest_path)

if __name__ == '__main__':
    unittest.main()