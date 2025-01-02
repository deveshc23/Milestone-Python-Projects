from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocators
from parsers.book import BookParser
import re

class BooksPage:

    def __init__(self,page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator=BooksPageLocators.BOOK
        book_tags=self.soup.select(locator)
        return [BookParser(e) for e in book_tags]
    
    @property
    def page_count(self):
        content=self.soup.select_one(BooksPageLocators.PAGER).string
        pattern='Page [0-9]+ of ([0-9]+)'
        matcher=re.search(pattern,content)
        pages=int(matcher.group(1))
        return pages