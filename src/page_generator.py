import os
from markdown_to_html_node import markdown_to_html_node
from block_markdown import extract_title

def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} using {template_path} -> {to_path}")
    with open(from_path, "r") as from_file:
        markdown = from_file.read()
    with open(template_path, "r") as template_file:
        template = template_file.read()
    markdown_title = extract_title(markdown)
    markdown_node = markdown_to_html_node(markdown)
    html = markdown_node.to_html()
    page = template.replace("{{title}}", markdown_title).replace("{{content}}", html)
    directory = os.path.dirname(to_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    with open(to_path, "w") as to_file:
        to_file.write(page)