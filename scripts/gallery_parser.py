from bs4 import BeautifulSoup

class GalleryPage:
    def __init__(self, filedir="apps/gallery/index.html",
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

    @property
    def pictures(self):
        pictures = []
        pictures.append(self.main.find(id="items-col1").contents)
        pictures.append(self.main.find(id="items-col2").contents)

        return pictures