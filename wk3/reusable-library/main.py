import webapp2
from library import Item, Price
from pages import FormPage, ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()
        r = ResultsPage()
        di = Item()
        pi = Price()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
