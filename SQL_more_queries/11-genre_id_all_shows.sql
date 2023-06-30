-- Comment
SELECT tv_shows.title, tv_show_genres.genre.id
FROM tv_shows
LEFT JOIN tv_show_genre ON tv_shows.id = tv_show_genre.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;