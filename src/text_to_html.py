from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORM_TEXT:
        return LeafNode(text_node.text, tag=None, props=None)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode(text_node.text, tag="b", props=None)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode(text_node.text, tag="i", props=None)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode(text_node.text, tag="code", props=None)
    elif text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode(text_node.text, tag="a", props=props)
    elif text_node.text_type == TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("", tag="img", props=props)
    else:
        raise Exception("Invalid text type")