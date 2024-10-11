import unittest
from inline_MD import split_nodes_delimiter
from textnode import *

class TestInlineTextNodeParsing(unittest.TestCase):
   
    def test_no_plain_text(self):
        tst = split_nodes_delimiter([TextNode("hi", text_type_italic)], "*", text_type_italic)
        self.assertEqual(tst, [TextNode("hi", text_type_italic)])

    def test_text_with_bold(self):
        tst = split_nodes_delimiter([TextNode("hi **whats up** dude", text_type_text)], "**", text_type_bold)
        self.assertEqual(tst, [TextNode("hi ", text_type_text), TextNode("whats up", text_type_bold), TextNode(" dude", text_type_text)])

    def test_text_with_mult_ital(self):
        tst = split_nodes_delimiter([TextNode("helloo *whatsaap*", text_type_text),
                                     TextNode("olaaa *comestes* amigos *ola* avantuuro", text_type_text)],"*", text_type_italic)
        self.assertEqual(tst, [TextNode("helloo ", text_type_text), TextNode("whatsaap", text_type_italic),
                                TextNode("olaaa ", text_type_text), TextNode("comestes", text_type_italic),
                                TextNode(" amigos ", text_type_text), TextNode("ola", text_type_italic), TextNode(" avantuuro", text_type_text)])
       
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )