import webapp2
from library import Item
from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        i = Item()
        p.css = "css/main.css"
        p.title = 'Albert Martinez | Reusable Library | DPW-1606 WDDBS Full Sail University'
        if self.request.GET:
            # store info from the form
            item_name = self.request.GET['item_name']
            original_price = self.request.GET['original_price']
            discount = self.request.GET['discount']
            qty = self.request.GET['qty']

            # replace the empty body attribute with the result html content since we know the form has
            # been submitted and user data has been stored
            p.body = '''
            <header>
            <h2>Details</h2>
        </header>
        <div class ="details">
            <p> The {self.item_name} was originally priced at ${self.original_price}.The item's new price with the
            {discount}% discount is: </p>
            <p id ="discount_price">${discount_price}</p>
        </div>
            '''
            # use the stored user entered data and populate the placeholder fields in the result page
            # using the locals() method we can pupulate these placeholder fields with stored user data
            p.body = p.body.format(**locals())
            # now that all data is filled in and ready to show, write all data to the browser for the user to see
            self.response.write(p.complete_page)
        else:
            # if no data has been entered via the form then load the page with the empty form
            p.body = p.form
            self.response.write(p.complete_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
