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
    if markdown[0] == ">":
        for line in lines:
            if line[0] != ">":
                return block_type_paragraph
        return block_type_quote
    if markdown[:2] == "* " or markdown[:2] == "- ":
        for line in lines:
            if line[:2] != "* " and line[:2] != "- ":
                return block_type_paragraph
        return block_type_ulist
    if markdown[:3] == "1. ":
        for i in range(len(lines)):
            if lines[i][:3] != f"{i+1}. ":
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph