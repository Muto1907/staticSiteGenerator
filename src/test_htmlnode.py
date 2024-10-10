import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        tmp = HTMLNode("h1", "Titleee", [HTMLNode("p")], {"href": "https://google.de",})
        htm = tmp.props_to_html()
        self.assertEqual(htm, ' href="https://google.de"')

    def test_repr(self):
        tmp = HTMLNode("h1", "Titleee", [HTMLNode("p")], {"href": "https://google.de",})
        str = tmp.__repr__()
        self.assertEqual(str, "HTMLNODE(h1, Titleee, [HTMLNODE(p, None, None, None)], {'href': 'https://google.de'})")


    def test_props2(self):
        tmp = HTMLNode("h1", "Titleee", [HTMLNode("p")], {"href": "https://google.de", "target": "blank", "animal": "cat"})
        htm = tmp.props_to_html()
        self.assertEqual(htm, ' href="https://google.de" target="blank" animal="cat"')

