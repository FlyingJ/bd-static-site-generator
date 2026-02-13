import unittest

from generate_page import generate_page

class TestGeneratePage(unittest.TestCase):
    def test_0(self):
        basepath = ''
        from_path = ''
        template_path = ''
        dest_path = ''
        with self.assertRaises(Exception):
            generate_page(basepath, from_path, template_path, dest_path)

    def test_1(self):
        basepath = '/'
        from_path = './test_markdown.md'
        template_path = './test_template.html'
        dest_path = './test_output.html'
        self.assertTrue(generate_page(basepath, from_path, template_path, dest_path))

    def test_1(self):
        basepath = '/'
        from_path = './test_markdown.2.md'
        template_path = './test_template.html'
        dest_path = './test_output.2.html'
        self.assertTrue(generate_page(basepath, from_path, template_path, dest_path))

if __name__ == '__main__':
    unittest.main()