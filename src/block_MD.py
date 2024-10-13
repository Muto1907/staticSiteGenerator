

def markdown_to_blocks(markdown):
    res = []
    mkdwn = markdown.split("\n\n")
    for mk in mkdwn:        
        mk = mk.strip()
        if mk == "":
            continue
        res.append(mk)
    return res
