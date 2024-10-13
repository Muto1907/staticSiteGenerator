import unittest
from block_MD import markdown_to_blocks, block_to_block_type



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