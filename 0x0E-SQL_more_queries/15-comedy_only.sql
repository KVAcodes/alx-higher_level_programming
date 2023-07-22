-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title FROM tv_genres as tvg 
INNER JOIN tv_show_genres as tvsg 
ON tvg.id = genre_id 
INNER JOIN tv_shows as tvs 
ON show_id = tvs.id 
WHERE name = 'Comedy' 
ORDER BY title;
