import media
import fresh_tomatoes

star_wars = media.Movie("Star Wars", "A space opera", "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg", "https://www.youtube.com/watch?v=1g3_CFmnU7k")

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [star_wars, toy_story]

fresh_tomatoes.open_movies_page(movies)
