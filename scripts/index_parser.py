from bs4 import BeautifulSoup

class IndexPage:
    def __init__(self, filedir="index.html",
                       encoding="utf-8",
                       parser="lxml"
        ):
        self.filedir = filedir
        self.soup = BeautifulSoup(open(filedir, "r", encoding=encoding), features=parser)

    def save(self):
        with open(self.filedir, "w", encoding="utf-8") as f:
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
    def slogan(self):
        return self.soup.find(id="slogan")

    @property
    def intro(self):
        return self.soup.find(id="intro")

    @property
    def squares(self):
        return self.soup.find(id="tiles").children

    @property
    def footer(self):
        return self.soup.find(id="footer")

    @property
    def manu_items(self):
        return self.menu.find('ul').contents