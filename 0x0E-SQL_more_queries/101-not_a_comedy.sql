-- lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT title FROM tv_shows
WHERE title NOT IN (
	SELECT title FROM tv_genres AS tvg 
	INNER JOIN tv_show_genres AS tvsg 
	ON tvg.id = genre_id 
	INNER JOIN tv_shows AS tvs 
	ON show_id = tvs.id 
	WHERE name = 'Comedy' 
	ORDER BY title
)
ORDER BY title;
