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

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            result.append(node)
            continue    
        props = extract_markdown_images(node.text)
        if props == []:
            result.append(node)
            continue
        txt = node.text
        for alt, src in props:
            splt = txt.split(f"![{alt}]({src})", 1)
            if len(splt) != 2:
                raise ValueError("Markdown Syntax Error, unclosed image tag")
            if splt[0] != "":
                result.append(TextNode(splt[0], text_type_text))
            result.append(TextNode(alt, text_type_image, src))
            txt = splt[1]
        if txt != "":
            result.append(TextNode(txt, text_type_text))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            result.append(node)
            continue     
        props = extract_markdown_links(node.text)
        if props == []:
            result.append(node)
            continue 
        txt = node.text
        for alt, src in props:
            splt = txt.split(f"[{alt}]({src})", 1)
            if len(splt) != 2:
                raise ValueError("Markdown Syntax Error, unclosed link tag")
            if splt[0] != "":
                result.append(TextNode(splt[0], text_type_text))
            result.append(TextNode(alt, text_type_link, src))
            txt = splt[1]
        if txt != "":
            result.append(TextNode(txt, text_type_text))
    return result

def text_to_textnodes(text):
    text_node = TextNode(text, text_type_text)
    tmp = split_nodes_delimiter([text_node], "**", text_type_bold)
    tmp = split_nodes_delimiter(tmp, "*", text_type_italic)
    tmp = split_nodes_delimiter(tmp, "`", text_type_code)
    tmp = split_nodes_image(tmp)
    tmp = split_nodes_link(tmp)
    return tmp
    