import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_constr(self):
        tst = LeafNode("this is a heading","h1")
        self.assertEqual("<h1>this is a heading</h1>", tst.to_html())

    def test_props(self):
        tst = LeafNode("this is a heading","h1", {"href": "https://google.de"})
        self.assertEqual('<h1 href="https://google.de">this is a heading</h1>', tst.to_html())

    def test_mult_props(self):
        tst = LeafNode("this is a paragraph", "p", {"href": "https://moeway.com", "class": "texto"})
        self.assertEqual('<p href="https://moeway.com" class="texto">this is a paragraph</p>', tst.to_html())

    def test_no_tag(self):
        tst = LeafNode("Hello za worldo!", None)
        self.assertEqual("Hello za worldo!", tst.to_html())