-- This lists all shows without the genre Comedy in database hbtn_0d_tvshows
   -- Each of the record should display:
      -- tv_shows.title
   -- The results must be sorted in ascending order by the show title
   -- The database name will be passed as argument of the mysql command

SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
      JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy" )
ORDER BY tv_shows.title;
