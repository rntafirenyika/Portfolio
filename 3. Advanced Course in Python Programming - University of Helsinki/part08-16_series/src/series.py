#class to handle series(seasons) information and searching thereof
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        
    def __str__(self):
        if not self.ratings:
            ratings_string = "no ratings"
        else:
            ratings_string = f"{len(self.ratings)} ratings, average {(sum(self.ratings) / len(self.ratings)):.1f} points"
        genre_list = self.genres
        genre_string = ", ".join(genre_list)
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{ratings_string}"

    # Adds a rating between 0 and 5 to any series object.    
    def rate(self, rating: int):
        self.ratings.append(rating)

# Allows searching through a list of series. 
def minimum_grade(rating: float, series_list: list):
    results = []
    for series in series_list:
        grade = sum(series.ratings) / len(series.ratings)
        if grade >= rating:
            results.append(series)
    return results

# Allows searching through a list of series.            
def includes_genre(genre: str, series_list: list):
    results = []
    for series in series_list:
        if genre in series.genres:
            results.append(series)
    return results