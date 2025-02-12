import unittest
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHtml(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        node = TextNode("Hello, world!", TextType.NORM_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("Hello, world!", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_italic(self):
        node = TextNode("Hello, world!", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)

    def test_text_node_to_html_node_code(self):
        node = TextNode("Hello, world!", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value, "Hello, world!")
        self.assertIsNone(html_node.props)
    def test_text_node_to_html_node_link(self):
        node = TextNode("Click me!", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me!")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props["href"], "https://www.google.com")

    def test_text_node_to_html_node_image(self):
        node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # empty string for images
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "Alt text")

if __name__ == "__main__":
    unittest.main()