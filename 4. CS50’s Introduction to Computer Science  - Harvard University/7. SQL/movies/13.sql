SELECT DISTINCT(name) FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE title IN (SELECT title FROM movies, stars, people WHERE movies.id = stars.movie_id AND stars.person_id = people.id AND name ='Kevin Bacon' AND birth = 1958)
AND name NOT IN ('Kevin Bacon');