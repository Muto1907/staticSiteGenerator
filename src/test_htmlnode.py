import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        tmp = HTMLNode("h1", "Titleee", [HTMLNode("p")], {"href": "https://google.de",})
        str = tmp.__repr__()
        self.assertEqual(str, "HTMLNODE(h1, Titleee, [HTMLNODE(p, None, None, None)], {'href': 'https://google.de'})")

    def test_propps(self):
        tmp = HTMLNode("h1", "Titleee", [HTMLNode("p")], {"href": "https://google.de",})
        htm = tmp.props_to_html()
        self.assertEqual(htm, ' href="https://google.de"')

    def test_props2(self):
        tmp = HTMLNode("h1", "Titleee", [HTMLNode("p")], {"href": "https://google.de", "target": "blank", "animal": "cat"})
        htm = tmp.props_to_html()
        self.assertEqual(htm, ' href="https://google.de" target="blank" animal="cat"')

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

    def test_parent_with_leafs_only(self):
        node = ParentNode(
    "p",
    [
        LeafNode("Bold text", "b"),
        LeafNode("Normal text", None),
        LeafNode("italic text", "i"),
        LeafNode("Normal text", None),
    ],
    )

        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_parent_with_other_parents(self):
        node = ParentNode(
    "div",
    [
        ParentNode("div",[
        LeafNode("Bold text", "b"),
        LeafNode("Normal text", None),
        LeafNode("italic text", "i"),
        LeafNode("Normal text", None),]
        , {"class": "container"})
    ]
    )

        self.assertEqual(node.to_html(),'<div><div class="container"><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></div>'
                         )




if __name__ == "__main__":
    unittest.main()