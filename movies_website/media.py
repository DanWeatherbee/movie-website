# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser
class Movie():
    ''' This class provides a way to store movie related information '''

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movieTitle, movieStoryLine, posterImage,	trailerYoutube, director, actors, rating):
            self.title = movieTitle
            self.storyline = movieStoryLine
            self.poster_image_url = posterImage
            self.trailerYoutubeUrl = trailerYoutube
            self.director = director
            self.actors = actors
            self.rating = rating

    def showTrailer(self):

        webbrowser.open(self.trailerYoutubeUrl)


    # initialize instance of class Movie
