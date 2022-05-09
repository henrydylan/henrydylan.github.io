from bs4 import BeautifulSoup

class ArtNavPage:
    def __init__(self, filedir="pages/art.html",
                       encoding="utf-8",
                       parser="lxml"
        ):
        self.filedir = filedir
        self.soup = BeautifulSoup(open(filedir, "r", encoding=encoding), features=parser)

    def save(self):
        with open(self.filedir, "w", encoding="utf-8") as f:
            f.write(self.soup.prettify())

    @property
    def title(self):
        return self.soup.find("title")

    @property
    def main(self):
        return self.soup.find(id="main")

    def insert_article(self, title, href):
        br = self.soup.new_tag('br')
        self.main.find('div').append(br)
        a = self.soup.new_tag('a')
        a.string = title
        a['href'] = href
        self.main.find('div').append(a)
        self.save()

    def remove_article(self, index):
        assert index >= 0
        self.main.find('div').find_all()[index * 2 + 2].decompose()
        if index > 0:
            self.main.find('div').find_all()[index * 2 + 1].decompose()
        self.save()