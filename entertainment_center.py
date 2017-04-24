"""
simple file for Udacity project. Create moveis with imported media.py Movies
class. Need to give the following with creating an object media.Movie():
    string - movie title
    string - story synopsis
    string - movie poster url
    string - youtube movie trailer URL
"""

import media
import fresh_tomatoes

star_wars = media.Movie("Star Wars", "A space opera",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

your_name = media.Movie("Your Name", "The story of a high school girl in rural Japan and a high school boy in Tokyo who swap bodies",
                        "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
                        "https://www.youtube.com/watch?v=e4dZhQaTJMk")

# Create a list with the movie objects you made
movies = [your_name, toy_story, star_wars]

# Pass the movies list into the provided fresh_tomatoes.open_movies_page() function
fresh_tomatoes.open_movies_page(movies)
