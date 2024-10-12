from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in ['*', '**', '`',]:
        raise Exception("Markdown Syntax Exception: Invalid choice of Delimiter")
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            splt = node.text.split(delimiter)
            if len(splt) % 2 == 0:
                raise ValueError("No Matching Delimiter found")

            for i in range(0,len(splt)):
                if splt[i] == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(splt[i], text_type_text))
                    
                else:
                    new_nodes.append(TextNode(splt[i], text_type))
                    
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    result = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return result

def extract_markdown_links(text):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result