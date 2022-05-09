from scripts.gallery_parser import GalleryPage
from .index_parser import IndexPage
from .generic_parser import GenericPage
from .art_nav_parser import ArtNavPage
import markdown
from bs4 import BeautifulSoup

def create_generic_from_markdown(filedir):
    generic = GenericPage()
    with open(filedir, "r", encoding="utf-8") as f:
        markdown_doc = f.read()
    html_doc = markdown.markdown(markdown_doc, extensions=['md4mathjax'])
    content_tags = BeautifulSoup(html_doc, features="lxml").find_all()
    inner = generic.main.find("div")
    inner.clear()
    for c in content_tags:
        inner.append(c)
    return generic


def create_page(markdown_filedir, html_filedir):
    generic = create_generic_from_markdown(markdown_filedir)
    generic.save(html_filedir)


def change_square_link(i, href):
    index = IndexPage()
    a = index.soup.find(id='tiles').find_all('a')[i]
    a['href'] = href
    index.save()


def change_square_text(i, text):
    index = IndexPage()
    h2 = index.soup.find(id='tiles').find_all('h2')[i]
    h2.string = text
    index.save()


def change_square_description(i, description):
    index = IndexPage()
    p = index.soup.find(id='tiles').find_all('p')[i]
    p.string = description.replace("-", " ")
    index.save()
    

def change_gallery_picture(row, col, full_dir, thumb_dir):
    gallery = GalleryPage()
    picture = gallery.pictures[row][col+1] # 1st and last item is '\n', don't know why
    # assert picture.name == "article", f"tag name {picture.name}: can only set a picture"
    picture.find('a').href = full_dir
    picture.find('img').href = thumb_dir
    gallery.save()


def insert_article(title, href):
    artnav = ArtNavPage()
    artnav.insert_article(title, href)
    artnav.save()


def remove_article(index):
    artnav = ArtNavPage()
    artnav.remove_article(index)
    artnav.save()
