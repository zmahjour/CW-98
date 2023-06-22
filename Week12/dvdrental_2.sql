SELECT title, length
FROM film
WHERE length > (SELECT AVG(length) FROM film);


SELECT film.film_id, title, return_date
FROM film
JOIN inventory ON inventory.film_id = film.film_id
JOIN rental ON rental.inventory_id = inventory.inventory_id
WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30'