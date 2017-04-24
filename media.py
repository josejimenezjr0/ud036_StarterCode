"""
media.py contains a Movie class that will genarate a data structure with a
movie's title, storyline, poster, and trailerself.
"""

class Movie(object):
    """ Movie init takes in strings for title title, storyline, poster, and
        trailer. There is a class variable that containg the movie rating
        system of G, PG, PG-13, and R.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, m_title, m_storyline, m_poster, m_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster
        self.trailer_youtube_url = m_trailer
