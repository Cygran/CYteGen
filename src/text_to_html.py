from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORM_TEXT:
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == TextType.BOLD_TEXT:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.ITALIC_TEXT:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE_TEXT:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img", "", props)
    else:
        raise Exception("Invalid text type")