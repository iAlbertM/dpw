from __future__ import division
import webapp2
from library import PriceChecker
from pages import FormPage, ResultPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
        fp = FormPage()
        rp = ResultPage()
        i = PriceChecker()
        page = ''

        if self.request.GET:
            # store info from the form
            i.item = self.request.GET['item']
            i.price = self.request.GET['price']
            i.discount = self.request.GET['discount']
            i.qty = self.request.GET['qty']
            i.discount_decimal = str(i.get_discount_decimal(float(i.discount)))
            i.discount_amount = str(i.get_discount_amount(float(i.discount_decimal),float(i.price)))
            i.discount_price = str(i.get_discount_price())
            i.discount_qty = str(i.get_discount_qty())
            rp.body = '''
                    <header>
                        <h1>PriceCheckr</h1>
                    </header>
                    <div class="details">
                        <h2>Check Out the Details of Your Item</h2>
                        <p> The <strong>{i.qty} {i.item}</strong>\'s original price is <strong class="green">${i.price}</strong>, <i>but</i>, when you apply the <strong class="green">{i.discount}%</strong> discount...</p>
                        <p>You end up with an awesome price of <span id ="large">${i.discount_price}!</p>
                    </div>
            '''
            rp.body = rp.body.format(**locals())
            self.response.write(rp.print_page())
        else:
            self.response.write(fp.print_page())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
