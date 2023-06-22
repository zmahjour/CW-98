SELECT title, category.name, release_year
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id;


SELECT title, category.name, release_year
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name IN ('Action', 'Comdedy', 'Family');


SELECT category.name, COUNT(*) AS number_of_its_films
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name;


SELECT category.name, COUNT(*) AS number_of_films
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name
HAVING COUNt(*) BETWEEN 60 AND 68;


SELECT title, category.name AS category, language.name AS language
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN language ON language.language_id = film.language_id;


