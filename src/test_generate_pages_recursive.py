import unittest

from generate_pages_recursive import generate_pages_recursive

class TestGeneratePagesRecursive(unittest.TestCase):
    def test_0(self):
        dir_path_content = './test_content'
        template_path = './test_template.html'
        dest_dir_path = './test_public'
        self.assertTrue(generate_pages_recursive(dir_path_content, template_path, dest_dir_path))

    def test_1(self):
        dir_path_content = ''
        template_path = ''
        dest_dir_path = ''
        with self.assertRaises(Exception) as e:
            result = generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

if __name__ == '__main__':
    unittest.main()