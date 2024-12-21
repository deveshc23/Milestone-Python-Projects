from os import remove
from .database_connection import DatabaseConnection


def create_books_table():
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(names text primary key,author text,read integer)')


def add_book(name,author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))
    # \",0); DROP TABLE books; if this is used in place of author the table will be deleted...
    # Hence, this is called SQL injection attack and would delete the data got.
    # So you cant directly substitute this as people might write such a code and drop the code

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM books')
        books=[{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()] #as we did not make any changes we did not write commit

def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))


