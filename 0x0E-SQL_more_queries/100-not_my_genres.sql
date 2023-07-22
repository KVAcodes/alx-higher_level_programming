-- uses the hbtn_0d_tvshows database to lists all genres not linked to the show Dexter.

SELECT name FROM tv_genres
WHERE name NOT IN (
	SELECT name FROM tv_genres AS tvg 
	INNER JOIN tv_show_genres AS tvsg 
	ON tvg.id = genre_id 
	INNER JOIN tv_shows AS tvs 
	ON show_id = tvs.id 
	WHERE title = 'Dexter' 
	ORDER BY name)
ORDER BY name;
