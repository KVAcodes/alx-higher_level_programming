-- lists all cities contained in the database hbtn_0d_usa

SELECT cities.id AS id,
       cities.name AS name
  FROM cities
  JOIN states.name AS name
    ON cities.id = states.id
 GROUP BY id ASC; 
