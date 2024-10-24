import os
import shutil
from block_MD import *
def Cpy_Directory(source, destination):
    if not os.path.exists(source):
        raise Exception("path to source directory does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    items = os.listdir(source)
    for item in items:
        pth = os.path.join(source, item)
        if os.path.isfile(pth):
            #print(f"Copying {pth}...")
            shutil.copy(pth, destination)
        else:
            Cpy_Directory(pth, destination+ f"/{item}")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    markdown_content = markdown_file.read()
    template_file = open(template_path)
    template_content = template_file.read()
    template_file.close()
    markdown_file.close()
    html = markdown_to_html_node(markdown_content)
    html_str = html.to_html()
    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_str)
    path = os.path.dirname(dest_path)
    if path != "":
        os.makedirs(path, exist_ok=True)
    dest_file = open(dest_path, "w")
    dest_file.write(template_content)
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        pth = os.path.join(dir_path_content, entry)
        dest_pth = os.path.join(dest_dir_path, entry).replace("md", "html")
        if os.path.isfile(pth):
            if pth.endswith(".md"):
                generate_page(pth, template_path, dest_pth)
        else:
            generate_pages_recursive(pth, template_path, os.path.join(dest_dir_path, entry))
        