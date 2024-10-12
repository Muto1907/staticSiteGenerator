import unittest
from inline_MD import *
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

class TestMarkdownExtraction(unittest.TestCase):
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print(extract_markdown_images(text))
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")] )
        # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    def test_split_img(self):
        node = TextNode(
        "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
        text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with an image ", text_type_text),
            TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
            "to youtube", text_type_image, "https://www.youtube.com/@bootdotdev"
            ),
            ])
    
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,
            [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ), 
            ]
        )
    def test_split_plain(self):
        node = TextNode("only text", text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [node])
