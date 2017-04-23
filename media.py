import webbrowser

#class Video():
#    def __init__(self, ):


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, m_title, m_storyline, m_poster, m_trailer):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = m_poster
        self.trailer_youtube_url = m_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

#class TvShow():
#    def __init__(self, title):
#        self.title

#    def get
