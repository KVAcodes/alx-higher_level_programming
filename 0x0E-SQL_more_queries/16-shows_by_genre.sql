-- lists all shows, and all genres linked to that show.
SELECT title, name 
FROM tv_genres AS tvg 
INNER JOIN tv_show_genres AS tvsg 
ON tvg.id = genre_id 
RIGHT JOIN tv_shows AS tvs 
ON show_id = tvs.id  
ORDER BY title, name;
