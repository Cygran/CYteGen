import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("Hello world", TextType.NORM_TEXT)
        node2 = TextNode("Goodbye world", TextType.NORM_TEXT)
        self.assertNotEqual(node1, node2)

    def test_different_types(self):
        node1 = TextNode("Test text",TextType.ITALIC_TEXT, "https://test.abc")
        node2 = TextNode("Test text",TextType.BOLD_TEXT, "https://test.abc")
        self.assertNotEqual(node1, node2)

    def test_url_vs_urlNone(self):
        node1 = TextNode("Test text",TextType.ITALIC_TEXT, "https://test.abc")
        node2 = TextNode("Test text",TextType.ITALIC_TEXT)
        self.assertNotEqual(node1, node2)

    def test_same_text_same_url_different_type(self):
        node1 = TextNode("Click here", TextType.BOLD_TEXT, "https://boot.dev")
        node2 = TextNode("Click here", TextType.ITALIC_TEXT, "https://boot.dev")
        self.assertNotEqual(node1, node2)

    def test_different_urls_same_everything_else(self):
        node1 = TextNode("Visit us", TextType.ITALIC_TEXT, "https://boot.dev")
        node2 = TextNode("Visit us", TextType.ITALIC_TEXT, "https://google.com")
        self.assertNotEqual(node1, node2)

    def test_eq_with_urls(self):
        node1 = TextNode("Visit Boot.dev", TextType.BOLD_TEXT, "https://boot.dev")
        node2 = TextNode("Visit Boot.dev", TextType.BOLD_TEXT, "https://boot.dev")
        self.assertEqual(node1, node2)

    def test_eq_with_empty_text(self):
        node1 = TextNode("", TextType.ITALIC_TEXT, "https://boot.dev")
        node2 = TextNode("", TextType.ITALIC_TEXT, "https://boot.dev")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()