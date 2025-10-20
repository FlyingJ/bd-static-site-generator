import unittest

from utils import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownUtils(unittest.TestCase):
    def test_extract_markdown_images_0(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expectation = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expectation)
        
    def test_extract_markdown_links_0(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expectation = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expectation)
    
    def test_extract_markdown_images_1(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        result = extract_markdown_images(text)
        expectation = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(result, expectation)

if __name__ == '__main__':
    unittest.main()
