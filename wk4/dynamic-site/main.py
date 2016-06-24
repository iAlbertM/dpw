import webapp2
from data import Character


class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = Character()
        c1 = c.characters[0].name
        print c.characters[0].name

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
