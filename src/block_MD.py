from htmlnode import *
from textnode import *
from inline_MD import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    res = []
    mkdwn = markdown.split("\n\n")
    for mk in mkdwn:        
        mk = mk.strip()
        if mk == "":
            continue
        res.append(mk)
    return res

def block_to_block_type(markdown):        
    lines = markdown.split("\n")
    if markdown[0] == "#":
        for i in range(1,7):
            if markdown[i] == " ":
                return block_type_heading
            if markdown[i] == "#":
                continue
            return block_type_paragraph
    if markdown[:3] == "```" and markdown[-3:] == "```" and len(lines) > 1:
        return block_type_code
    if markdown.strip().startswith(">"):
        for line in lines:
            if not line.strip().startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if markdown.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if markdown[:3] == "1. ":
        for i in range(len(lines)):
            if lines[i][:3] != f"{i+1}. ":
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    div = ParentNode("div", [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        html_block_node = create_html_node_block(block, type)
        div.children.append(html_block_node)
    return div

def create_html_node_block(markdown, type):
    if type == block_type_paragraph:
        return ParentNode("p", text_to_children(" ".join(markdown.split("\n"))))
    if type == block_type_heading:
        if markdown.startswith("###### "):
            return ParentNode("h6", text_to_children(markdown[7:])) 
        if markdown.startswith("##### "):
            return ParentNode("h5", text_to_children(markdown[6:]))
        if markdown.startswith("#### "):
            return ParentNode("h4", text_to_children(markdown[5:]))
        if markdown.startswith("### "):
            return ParentNode("h3", text_to_children(markdown[4:]))
        if markdown.startswith("## "):
            return ParentNode("h2", text_to_children(markdown[3:]))
        if markdown.startswith("# "):
            return ParentNode("h1", text_to_children(markdown[2:]))
    if type == block_type_code:
        return ParentNode("pre", [ParentNode("code", text_to_children(markdown[3:-3]))])
    if type == block_type_olist:
        items = markdown.split("\n")
        html_items = []
        for item in items:
            text = item[3:]
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
        return ParentNode("ol", html_items)
    if type == block_type_quote:
        lines = markdown.split("\n")
        new_lines = []
        for i in range(len(lines)):
            new_lines.append(lines[i].lstrip(">").strip())
        content = " ".join(new_lines)
        return ParentNode("blockquote", text_to_children(content))
    if type == block_type_ulist:
        items = markdown.split("\n")
        html_items = []
        for item in items:
            text = item[2:]
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
        return ParentNode("ul", html_items)
    raise ValueError("Invalid Block Type")
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    res = []
    for node in text_nodes:
        res.append(text_node_to_html_node(node))
    return res
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    result = ""
    for block in blocks:
        if block.strip().startswith("# "):
            result = block.strip()[2:]
            break
    if result == "":
        raise Exception("No h1 heading found.")
    return result