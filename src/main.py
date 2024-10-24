from textnode import *
from filecpy import *
def main():
    Cpy_Directory("./static/", "./public/")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

if __name__ == "__main__":
    main()