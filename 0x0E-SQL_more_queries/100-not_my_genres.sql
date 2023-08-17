-- This list all genres not linked to the show Dexter
   -- Each of the record should display:
      -- tv_genres.name
   -- The results must be sorted in ascending order by the genre name
   -- The database name will be passed as argument of the mysql command

SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER" )
ORDER BY tv_genres.name;
