-- Lists all genres contained in hbtn_0d_tvshow
-- and displays numbers of shows that are linked
SELECT g.`name` AS `genre`, COUNT(sg.show_id) AS `number_of_shows`
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS sg ON g.`id` = sg.`genre_id`
GROUP BY g.`name`
HAVING `number_of_shows` > 0
ORDER BY `number_of_shows` DESC;
