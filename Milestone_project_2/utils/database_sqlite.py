from os import remove
import sqlite3


def create_books_table():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(names text primary key,author text,read integer)')
    connection.commit()
    connection.close()

# def _save_all_books(books): # _ at the beginning of the func name represents that the function is private in many languages(not Python)
#     with open(books_file,'w') as file:
#         json.dump(books,file)

def add_book(name,author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))
    # \",0); DROP TABLE books; if this is used in place of author the table will be deleted...
    # Hence, this is called SQL injection attack and would delete the data got.
    # So you cant directly substitute this as people might write such a code and drop the code
    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books=[{'name':row[0],'author':row[1],'read':row[2]} for row in cursor.fetchall()] #as we did not make any changes we did not write commit
    connection.close()

def mark_book_as_read(name):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))
    connection.commit()
    connection.close()

def delete_book(name):
    connection=sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name=?', (name,))
    connection.commit()
    connection.close()


