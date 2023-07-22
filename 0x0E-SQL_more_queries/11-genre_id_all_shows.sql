-- lists all shows contained in hbtn_0d_tvshows
SELECT tvs.title, tvg.genre_id 
FROM tv_shows AS tvs 
LEFT JOIN tv_show_genres AS tvg 
ON tvs.id = tvg.show_id 
ORDER BY 
	tvs.title ASC, 
	tvg.genre_id ASC;
