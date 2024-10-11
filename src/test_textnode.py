import unittest
from inline_MD import *
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

    def test_str(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.guuguru.com")
        self.assertNotEqual(node,node2)       
 
    def test_None(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

    def test_t_type(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node,node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_plain_text(self):
        txt = TextNode("plain text", text_type_text)
        lf = LeafNode("plain text")
        self.assertEqual(text_node_to_html_node(txt).value, lf.value)
        self.assertEqual(text_node_to_html_node(txt).tag, lf.tag)

    def test_bold_text(self):
        txt = TextNode("bold text", text_type_bold)
        lf = LeafNode("bold text", "b")
        self.assertEqual(text_node_to_html_node(txt).value, lf.value)
        self.assertEqual(text_node_to_html_node(txt).tag, lf.tag)

    def test_bold_italic(self):
        txt = TextNode("italic text", text_type_italic)
        lf = LeafNode("italic text", "i")
        self.assertEqual(text_node_to_html_node(txt).value, lf.value)
        self.assertEqual(text_node_to_html_node(txt).tag, lf.tag)

    def test_link(self):
        txt = TextNode("link", text_type_link, "https://google.de")
        lf = LeafNode("link", "a", {"href": "https://google.de"})
        self.assertEqual(text_node_to_html_node(txt).value, lf.value)
        self.assertEqual(text_node_to_html_node(txt).tag, lf.tag)
        self.assertEqual(text_node_to_html_node(txt).props["href"], lf.props["href"])

    def test_img(self):
        txt = TextNode("image", text_type_image, "https://google.de")
        lf = LeafNode("", "img", {"src": "https://google.de", "alt": "image"})
        self.assertEqual(text_node_to_html_node(txt).value, lf.value)
        self.assertEqual(text_node_to_html_node(txt).tag, lf.tag)
        self.assertEqual(text_node_to_html_node(txt).props["src"], lf.props["src"])
        self.assertEqual(text_node_to_html_node(txt).props["alt"], lf.props["alt"])

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
       

if __name__ == "__main__":
    unittest.main()

