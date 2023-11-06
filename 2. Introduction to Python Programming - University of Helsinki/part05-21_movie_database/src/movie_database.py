# Adds a new movie object into a movie database(list).
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}
    movie["name"] = name
    movie["director"] = director
    movie["year"] = year
    movie["runtime"] = runtime
    database.append(movie)