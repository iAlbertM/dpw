from __future__ import division
import webapp2
from library import SaleItem, PriceChecker
from pages import FormPage, ResultPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        fp = FormPage()
        rp = ResultPage()
        page = ''

        if self.request.GET:
            # store info from the form
            item = self.request.GET['item']
            price = self.request.GET['price']
            discount = self.request.GET['discount']
            qty = self.request.GET['qty']
            self.response.write("item: " + item + "Price: " + str(price) + "Discount: " + str(discount) + "Qty: " + str(qty))
            i = PriceChecker(item, price, discount, qty)
            qty = str(i.qty)
            item = str(i.item)
            discount = str(i.discount)
            discount_amount = str(i.discount_amount)
            discount_price = str(i.discount_price)
            discount_saving = str(i.discount_saving)
            rp.body = '''
                    <header>
                        <h1>PriceCheckr</h1>
                    </header>
                    <div>
                        <h2>Details</h2>
                    </div>
                    <div class="details">
                        <p> The {qty} {item} s original price of $ {price} ,
                        after applying the {discount} %  discount, the new price is $ {discount_price} </p>
                    </div>
            '''
            rp.print_page()
            rp.body = rp.body.format(**locals())
            self.response.write(rp.print_page())
        else:
            self.response.write(fp.print_page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
