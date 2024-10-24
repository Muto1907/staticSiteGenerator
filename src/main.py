from textnode import *
from filecpy import *
def main():
    Cpy_Directory("./static/", "./public/")
    generate_pages_recursive("./content/", "./template.html", "./public/")

if __name__ == "__main__":
    main()