
import webapp2
from library import MovieData
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # class for page
        p = Page()
        # movie title
        # year movie was made
        # director of the filew
        md1 = MovieData()
        md1.title = 'The Princess Bride'
        md1.year = 1989
        md1.director = 'Rob Reiner'

        md1 = MovieData()
        md1.title = 'Dune'
        md1.year = 1986
        md1.director = 'David Lynch'

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
