movies = []


def add_movies(movies):
    title = input("Enter the movie title:")
    director = input("Enter the name of the director:")
    year = input("Enter the year it was released:")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies(movies):
    for movie in movies:
        print(f"{movie['title']} was directed by {movie['director']} and released in the year {movie['year']}.")


def find_movies(movies):
    search_prompt = input("Enter the movie title you want to find: ")
    for movie in movies:
        if search_prompt.lower() == movie['title'].lower():  # Case-insensitive comparison
            print(f"Found it! The movie {movie['title']} by the director {movie['director']} was released in {movie['year']}.")
            break
    else:
        print("The movie was not found.")

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find your movie by title, 'q' to quit"

selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        add_movies(movies)
    elif selection == 'l':
        show_movies(movies)
    elif selection == 'f':
        find_movies(movies)
    else:
        print("Unknown command. please try again")

    selection = input(MENU_PROMPT)