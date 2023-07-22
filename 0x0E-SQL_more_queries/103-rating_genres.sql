-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.

SELECT name, SUM(tvsr.rate) AS rating 
FROM tv_genres AS tvg 
JOIN tv_show_genres AS tvsg 
ON tvg.id = tvsg.genre_id 
JOIN tv_show_ratings AS tvsr 
ON tvsg.show_id = tvsr.show_id 
GROUP BY name 
ORDER BY rating DESC;
