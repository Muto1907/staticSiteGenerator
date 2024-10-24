from textnode import *
from filecpy import *
def main():
    Cpy_Directory("/home/mahmut/workspace/github.com/Muto1907/staticSiteGenerator/static/", "/home/mahmut/workspace/github.com/Muto1907/staticSiteGenerator/public/")
    generate_page("/home/mahmut/workspace/github.com/Muto1907/staticSiteGenerator/content/index.md", "/home/mahmut/workspace/github.com/Muto1907/staticSiteGenerator/template.html", "/home/mahmut/workspace/github.com/Muto1907/staticSiteGenerator/public/index.html")

if __name__ == "__main__":
    main()