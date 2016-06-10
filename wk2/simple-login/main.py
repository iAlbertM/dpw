'''
Albert Martinez
06/09/16
DPW-1606
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self): # function to start it all up
        self.response.write("Hello World! It is I, Albert M!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
