from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(tag, value, None, props )

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        result = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return result
            
    def __repr__(self):
        return f"LEAFNODE({self.tag}, {self.value}, {self.props})"