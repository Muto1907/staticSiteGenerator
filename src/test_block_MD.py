import unittest
from block_MD import markdown_to_blocks

class Test_block_MD(unittest.TestCase):
    def test_block(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n\n          * This is the first list item in a list block\n* This is a list item\n* This is another list item"
        res = markdown_to_blocks(markdown)
        self.assertEqual(res, ["# This is a heading", 
                               "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                               "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                               ])
