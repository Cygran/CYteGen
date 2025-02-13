from textnode import TextNode, TextType
from copy_static import copy_static_files
from page_generator import generate_pages_recursive

def main():
    copy_static_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()
