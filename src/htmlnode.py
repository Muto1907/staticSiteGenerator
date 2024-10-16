class HTMLNode:
    def __init__(self, tag=None, value = None, children =None, props =None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
        
    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"


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
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return self.value == other.value and self.tag == other.tag and self.props == other.props
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children == None:
            raise ValueError("Parent nodes must have children")
        if self.tag == None:
            raise ValueError("Parent Nodes must have a tag")
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result           
    def __repr__(self):
        return f"PARENTNODE({self.tag}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return self.tag == other.tag and self.children == other.children
 