import requests

from pages.books_page import BooksPage

page_content=requests.get('http://books.toscrape.com').content
page=BooksPage(page_content)
books=page.books
for i in range(2,page.page_count+1):
    page_content=requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html').content
    page=BooksPage(page_content)
    books.extend(page.books)