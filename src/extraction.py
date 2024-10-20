from block_MD import *
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