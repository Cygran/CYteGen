import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiters(self):
        node = TextNode("This is **bold** text", TextType.NORM_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.NORM_TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.NORM_TEXT)

    def test_italic_delimiters(self):
        node = TextNode("This is *italic* text", TextType.NORM_TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.NORM_TEXT)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.NORM_TEXT)

    def test_code_delimiters(self):
        node = TextNode("This is `code` text", TextType.NORM_TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.NORM_TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.NORM_TEXT)

    def test_multiple_nodes(self):
        node1 = TextNode("This is **bold** text", TextType.NORM_TEXT)
        node2 = TextNode("and this is *italic* text", TextType.NORM_TEXT)
        nodes = [node1, node2]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.NORM_TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.NORM_TEXT)
        self.assertEqual(result[3].text, "and this is *italic* text")
        self.assertEqual(result[3].text_type, TextType.NORM_TEXT)

    def test_no_delimiters(self):
        node = TextNode("This is just plain text", TextType.NORM_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is just plain text")
        self.assertEqual(result[0].text_type, TextType.NORM_TEXT)

    def test_already_formatted(self):
        node = TextNode("This is already bold", TextType.BOLD_TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is already bold")
        self.assertEqual(result[0].text_type, TextType.BOLD_TEXT)

    def test_missing_delimiter(self):
        node = TextNode("This text has **only one delimiter", TextType.NORM_TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)