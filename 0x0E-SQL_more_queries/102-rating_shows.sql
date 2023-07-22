-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(tvsr.rate) AS rating 
FROM tv_shows AS tvs 
LEFT JOIN tv_show_ratings AS tvsr 
ON tvs.id = tvsr.show_id 
GROUP BY title 
ORDER BY rating DESC;
