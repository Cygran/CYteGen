from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type.NORM_TEXT:
            new_nodes.append(old_node)
        else:
            text = old_node.text
            # Find first delimiter
            first_delim = text.find(delimiter)
            if first_delim == -1:
                # No delimiter found, keep node as is
                new_nodes.append(old_node)
                continue
            #find closing delimiter
            second_delim = text.find(delimiter, first_delim + 1)
            if second_delim == -1:
                raise ValueError("No closing delimiter found!")
            before = text[:first_delim]
            between = text[first_delim + len(delimiter):second_delim]
            after = text[second_delim + len(delimiter):]
            
            # Create new nodes
            if before:
                new_nodes.append(TextNode(before, TextType.NORM_TEXT))
            new_nodes.append(TextNode(between, text_type))
            if after:
                new_nodes.append(TextNode(after, TextType.NORM_TEXT))

    return new_nodes