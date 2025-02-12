import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_none(self):
        # Test with None props
        node = HTMLNode(props=None)
        assert node.props_to_html() == ""

    def test_props_to_html_with_empty_dict(self):
        # Test with empty props dictionary
        node = HTMLNode(props={})
        assert node.props_to_html() == ""

    def test_props_to_html_with_one_prop(self):
        # Test with single property
        node = HTMLNode(props={"href": "https://www.google.com"})
        assert node.props_to_html() == ' href="https://www.google.com"'

    def test_props_to_html_with_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        assert node.props_to_html() == ' href="https://www.google.com" target="_blank"'

class TestLeafNode(unittest.TestCase):

    def test_leafnode_without_props(self):
        node = LeafNode(value="This is a test", tag="p")
        self.assertEqual(node.to_html(), "<p>This is a test</p>")

    def test_leafnode_with_props(self):
        node = LeafNode(value="Click here", tag="a")
        node.props = {"href": "https://example.com"}
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

    def test_leafnode_raw_value(self):
        node = LeafNode(value="This is raw text")
        self.assertEqual(node.to_html(), "This is raw text")

    def test_leafnode_missing_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(value=None, tag="p")
            node.to_html()

if __name__ == "__main__":
    unittest.main()