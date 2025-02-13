from textnode import TextNode, TextType

def main():
    node = TextNode("Hello", TextType.BOLD, "https://example.com")
    print(node)

main()
