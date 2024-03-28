-- database: c:\Users\Adriele\OneDrive\Desktop\BFH CLASSES\DataBase\movies2.db

-- Use the ▷ button in the top right corner to run the entire file.

SELECT * FROM "world-cities";



SELECT "world-cities".country, "world-cities".name
FROM "world-cities"
WHERE "world-cities".country IN ('Japan', 'England', 'Spain');

SELECT "world-cities".country, "world-cities".name
FROM "world-cities"
WHERE "world-cities".country='Japan'
UNION
SELECT "world-cities".country, "world-cities".name
FROM "world-cities"
WHERE "world-cities".country='England'
UNION
SELECT "world-cities".country, "world-cities".name
FROM "world-cities"
WHERE "world-cities".country='Spain';


SELECT directors.director_name, directors.salary
FROM directors
WHERE directors.salary >=1000000 and directors.salary<=2000000
