import webapp2
from library import SaleItem
from pages import FormPage, ResultPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        fp = FormPage()
        rp = ResultPage()

        if self.request.GET:
            # store info from the form
            item = self.request.GET['item_name']
            price = self.request.GET['original_price']
            discount = self.request.GET['discount']
            qty = self.request.GET['qty']
            i = SaleItem(item, price, discount, qty)
            rp.body = '''
                    <header>
                        <h1>PriceCheckr</h1>
                    </header>
                    <div>
                        <h2>Details</h2>
                    </div>
                    <div class="details">
                        <p> The {i.item} orignal price of ${i.price},
                        after applying the {i.discount}%  discount, the new price is:</p>
                        <p id="discount_price">${i.discount_price}</p>
                        <p id="savings">You just saved $<span>{i.discount_savings}</p>
                    </div>
            '''
            rp.body = rp.body.format(**locals())
            rp.print_page()

            self.response.write(i.get_discount_amount(discount))

            print(i.get_discount_price())
            print(i.get_discount_saving())

            self.response.write(rp.print_page())
        else:
            self.response.write(fp.print_page())

        # show discount amount
        # display final discount price
        # show user how much they saved

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
