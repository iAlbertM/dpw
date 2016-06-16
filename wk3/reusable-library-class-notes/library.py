class FavoriteMovies(object):
    def __init__(self):
        pass
        # array to hold movie info
        # add to array of movies
        # generate list of movies



class MovieData(object):
    def __init__(self):
        self.title = ''
        self.__year = 0 # check for valid year
        self.director = ''

    @property
    def year(self):
        pass

    @year.setter
    def year(self, y):
        if y > 2014: # if date is invalid
            print() 'Error, invalid date'
        else:
            self.__year = y