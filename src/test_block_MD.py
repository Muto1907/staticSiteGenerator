import unittest
from block_MD import *
from htmlnode import *



class Test_block_MD(unittest.TestCase):
    def test_block(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n          * This is the first list item in a list block\n* This is a list item\n* This is another list item"
        res = markdown_to_blocks(markdown)
        self.assertEqual(res, ["# This is a heading", 
                               "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                               "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                               ])

    def test_block_type_heading(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_type_code(self):
        block = "``` This is code\n and stuff```"
        self.assertEqual(block_to_block_type(block), "code")
    
    def test_block_type_quote(self):
        block = "> This is a qupte\n>mf"
        self.assertEqual(block_to_block_type(block), "quote")
    
    def test_block_type_fail_quote(self):
        block = ">This not a quote\n<mf\n\nhaha"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_type_unordered_list(self):
        block = "- This is an unordered list\n* ya feel me?\n- or nah?"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_type_ordered_list_fail(self):
        block = "1. This is an ordered list\n2. ya feel me?\n3. or nah?\n5. FAIL"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_type_ordered_list(self):
        block = "1. This is an ordered list\n2. ya feel me?\n3. or nah?"
        self.assertEqual(block_to_block_type(block), "ordered_list")

class Test_block_MD(unittest.TestCase):
    def test_simple_paragraph(self):
        md = "This is a simple Paragraph"
        html = markdown_to_html_node(md)
        self.assertEqual(html, ParentNode("div", [ParentNode("p", [LeafNode("This is a simple Paragraph")])]))

    def test_complex_markdown(self):
            md = """
            # Header 1

            This is a paragraph with **bold** and *italic* text.

            ## Header 2

            Here's a list:
            - Item 1
            - Item 2
            - Item 3

            And a block quote:

            > This is a block quote.
            > It can span multiple lines.

            Finally, here's some `inline code` and a code block:

            ```python
            def hello_world():
                print("Hello, World!")```"""
            html = markdown_to_html_node(md)
            self.assertEqual(html.tag, "div")
            self.assertEqual(len(html.children), 8)  # 8 main blocks now

            # Check header 1
            self.assertEqual(html.children[0].tag, "h1")
            self.assertEqual(html.children[0].children[0].value, "Header 1")

            # Check paragraph
            self.assertEqual(html.children[1].tag, "p")
            self.assertEqual(len(html.children[1].children), 5)  # Text, bold, text, italic, text
            self.assertEqual(html.children[1].children[1].tag, "b")
            self.assertEqual(html.children[1].children[3].tag, "i")

            # Check header 2
            self.assertEqual(html.children[2].tag, "h2")
            self.assertEqual(html.children[2].children[0].value, "Header 2")

            # Check list (currently a paragraph)
            self.assertEqual(html.children[3].tag, "p")
            self.assertTrue("Here's a list:" in html.children[3].children[0].value)

            # Check block quote (currently two paragraphs)
            self.assertEqual(html.children[4].tag, "p")
            self.assertEqual(html.children[4].children[0].value, "And a block quote:")

    def test_list_to_html(self):
        md = """- This is an unordered List
- How do you like it
- I dont give a snap
        

        # And this is a heading"""
        html = markdown_to_html_node(md)
        self.assertEqual(html.children[0], ParentNode("ul", [ParentNode("li", [LeafNode("This is an unordered List")]),
                                                           ParentNode("li", [LeafNode("How do you like it")]),
                                                           ParentNode("li",[LeafNode("I dont give a snap")])]))
        
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
            md = """
    > This is a
    > blockquote block

    this is paragraph text

    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
            )