from utils import database_sqlite

USER_CHOICE="""
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    database_sqlite.create_books_table()
    user_input=input(USER_CHOICE)
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()
        elif user_input=='l':
            list_books()
        elif user_input=='r':
            prompt_read_book()
        elif user_input=='d':
            prompt_delete_book()
        else:
            print("Unknown command, please try again ")

        user_input=input(USER_CHOICE)


def prompt_add_book():
    name=input('Enter the name of the book: ')
    author=input('Enter the author of the book: ')
    database_sqlite.add_book(name,author)


def list_books():
    books=database_sqlite.get_all_books()
    for book in books:
        read='YES' if book['read'] else 'NO'
        print(f" {book['name']} by {book['author']}, read: {book['read']}")

def prompt_read_book():
    name=input('Enter the name of the book you just finished reading: ')
    database_sqlite.mark_book_as_read(name)


def prompt_delete_book():
    name=input('Enter the name of the book you want to delete: ')
    database_sqlite.delete_book(name)

menu()