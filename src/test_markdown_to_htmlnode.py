import unittest

from markdown_to_htmlnode import markdown_to_htmlnode

# test_cases = [
#     (
#         x,
#         y
#     ),
#     (
#         x,
#         y
#     ),
# ]
class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote_0(self):
        old_maxDiff = self.maxDiff
        self.maxDiff = None
        md = '''# This is a Title

> This is the first line of a multiline
> block type quotation.
> -- Me

## Section 1

There is some text here.

## Section 2

I don't have much more to say, however, someone does:

> There is another quote here
> -- Someone

Lates
'''
        node = markdown_to_htmlnode(md)
        result = node.to_html()
        expectation = '''<div><h1>This is a Title</h1><blockquote><p>This is the first line of a multiline</p><p>block type quotation.</p><p>-- Me</p></blockquote><h2>Section 1</h2><p>There is some text here.</p><h2>Section 2</h2><p>I don't have much more to say, however, someone does:</p><blockquote><p>There is another quote here</p><p>-- Someone</p></blockquote><p>Lates</p></div>'''
        self.assertEqual(result, expectation)
        self.maxDiff = old_maxDiff

    def test_biggy(self):
        old_maxDiff = self.maxDiff
        self.maxDiff = None
        md = '''# This **is** a _heading_

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
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '''<div><h1>This <b>is</b> a <i>heading</i></h1><p>There is some regular text going on here now and there will be <i>italics</i> and <b>bold</b> stuff.</p><h2>There will be exposition and quotes</h2><p>There will be gobbldy gook written that will pass down the  ages, improving the lot of no one. Not once. Not ever.</p><p>So sayeth:</p><blockquote>That shit <i>Jay</i> said?That was some <b>bullshit</b>.Maddening, it is.</blockquote><h2>There will be lists</h2><ul><li>An <b>unordered</b> list item</li><li><i>Another</i> unordered list item</li></ul><h2>There may be numbered lists</h2><ol><li>Item 1</li><li><b>Item</b> 2</li><li>Item <b>3</b></li><li>Item 4</li></ol><h2>Some code</h2><pre><code>#include <stdio.h>\n\nint main()\n{\n    printf("Hello, World!\n");\n    return 0;\n}\n</code></pre><p>And a final plain, text paragraph.</p></div>'''
        )
        self.maxDiff = old_maxDiff

if __name__ == '__main__':
    unittest.main()
