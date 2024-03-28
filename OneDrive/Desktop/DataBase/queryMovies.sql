-- database: c:\Users\Adriele\OneDrive\Desktop\BFH CLASSES\DataBase\movies.db

-- Use the ▷ button in the top right corner to run the entire file.

SELECT * FROM "actors";

SELECT actors.actor_name AS "Actor",
actors.actor_movie AS "Film",
actors.salary AS "Salary" 
FROM actors 
WHERE actors.salary > 1000000;
 

 SELECT actors.actor_movie AS 'One Word Film Title'
 FROM actors
WHERE actors.actor_movie NOT LIKE '% %';


SELECT actresses.actress_movie
FROM actresses
WHERE actresses.actress_movie LIKE 'The%';

SELECT 'world-cities'.country, 'world-cities'.city_name
FROM 'world-cities'
WHERE country IN ('Japan', 'England', 'Spain');

SELECT count( DISTINCT actors.actor_name) As "How Many?",
avg(actors.salary) AS "Avarage Salary",
min(actors.salary) AS minimum,
max(actors.salary) AS maximum 
FROM actors;


SELECT count( DISTINCT actors.actor_name) As "How Many?",
avg(actors.salary) AS "Avarage Salary",
min(actors.salary) AS minimum,
max(actors.salary) AS maximum,
((100* (actors.salary - avg(actors.salary)) )/ ((avg(actors.salary)) ))AS derivation 
FROM actors