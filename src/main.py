from textnode import TextNode, TextType
from copy_static import copy_static_files
from page_generator import generate_page

def main():
    copy_static_files("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()
