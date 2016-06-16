if self.request.GET:
    # store info from the form
    item_name = self.request.GET['item_name']
    original_price = self.request.GET['original_price']
    discount = self.request.GET['discount']
    qty = self.request.GET['qty']
    # form data submitted + stored in variables I can use to populate placeholders
    results_body = '''
           <header>
               <h2>Details/h2>
           </header>
           <div class="details">
               <p>The {self.item_name} was originally priced at ${self.original_price}. The item's new price with
                   the {discount}% discount is:  </p>
               <p id="discount_price">${discount_price}</p>
           </div>
   '''
    # populate the placeholder content with data stored from the self.request.GET method
    results_body = results_body.format(**locals())
    # show page in browser with user data submitted via the form
    self.response.write(self.results_head + self.results_details + self.results_close)
else:
    # otherwise show the page with a blank form
    self.response.write(self.form_head + self.form_body + self.form_close)