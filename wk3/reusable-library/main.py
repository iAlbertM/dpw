import webapp2
# from library import Item, Price
# from pages import FormPage, ResultsPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        pass
        # i = Item(self)

    # i.item_name = self.request.GET['item_name']
    # i.original_price = self.request.GET['original_price']
    # i.discount = self.request.GET['discount']
    # i.qty = self.request.GET['qty']

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
