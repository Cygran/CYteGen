import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()