class HTMLNode:
    def __init__(self, value=None, tag=None, children=None, props=None):
        self.value = value
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props is None:
            return result
        for key in self.props.keys():
            value = self.props[key]
            result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, children=None, props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(value=None, tag=tag, children=children, props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("No Tag Value in Parent")
        if self.children is None:
            raise ValueError("No Child Value in Parent")
        props_html = self.props_to_html()
        result = f"<{self.tag}{props_html}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result