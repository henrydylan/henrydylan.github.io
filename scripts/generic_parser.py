from bs4 import BeautifulSoup

class GenericPage:
    def __init__(self, filedir="generic.html",
                       encoding="utf-8",
                       parser="lxml"
        ):
        self.filedir = filedir
        self.soup = BeautifulSoup(open(filedir, "r", encoding=encoding), features=parser)

    def save(self, filedir):
        with open(filedir, "w", encoding="utf-8") as f:
            f.write(self.soup.prettify())

    @property
    def header(self):
        return self.soup.find(id="header")

    @property
    def menu(self):
        return self.soup.find(id="menu")

    @property
    def main(self):
        return self.soup.find(id="main")

    @property
    def paragraphs(self):
        return self.main.children[0].children
    
    @property
    def footer(self):
        return self.soup.find(id="footer")