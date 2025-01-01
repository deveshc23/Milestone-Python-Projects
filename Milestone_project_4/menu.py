from app import books

USER_CHOICE="""Enter one of the following:
-'b' to look at the best books
-'c' to look at the cheapest books
-'n' to just get the next available book on the catalogue
-'q' to exit
"""
def print_best_books():
    best_books=sorted(books,key=lambda x: (x.rating*-1,x.price))[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_books=sorted(books,key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator=(x for x in books)

def get_next_book():
    print(next(books_generator))

def menu():
    user_input=input(USER_CHOICE)
    while user_input != 'q':
        if user_input=='b':
            print_best_books()
        elif user_input=='c':
            print_cheapest_books()
        elif user_input=='n':
            get_next_book()
        else:
            print("Unknown command. Please try again.")
        user_input=input(USER_CHOICE)

menu()
