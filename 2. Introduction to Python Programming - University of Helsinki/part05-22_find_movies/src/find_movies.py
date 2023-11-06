# Formulates a new list, which contains only the movies whose title includes the word searched for.
def find_movies(database: list, search_term: str):
    movies = []
    for movie in database:
        title = movie["name"].lower()
        if title.find(search_term.lower()) != -1:
            movies.append(movie)
    return movies