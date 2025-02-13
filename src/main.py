from textnode import TextNode, TextType
from copy_static import copy_static_files

def main():
    copy_static_files("static", "public")

main()
