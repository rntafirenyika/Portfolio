SELECT AVG(rating) from ratings
JOIN movies ON movies.id = ratings.movie_id
WHERE year = 2012;