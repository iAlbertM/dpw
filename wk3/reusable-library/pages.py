class Page(object):  # creating Page class to serve as template for other pages
    def __init__(self):  # initializing Page class
        # setting defualt values for Page class
        self.__title = 'My Title'  # private property to hold: html title
        self.__css = 'css/main.css'  # private property to hold: path to css file
        self.__js = 'js/main.js'  # private property to hold: path to js file
        self.__complete_page = ''

    @property
    def title(self):
        return self.__title

    @property
    def css(self):
        return self.__css

    @property
    def js(self):
        return self.__js

    @property
    def head(self):
        return self.__head

    @property
    def close(self):
        return self.__close

    @property
    def body(self):
        return self.__body

    @property
    def complete_page(self):
        return self.__complete_page

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @css.setter
    def css(self, new_css):
        self.__css = new_css

    @js.setter
    def js(self, new_js):
        self.__js = new_js

    @head.setter
    def head(self, new_head):
        self.__head = new_head

    @close.setter
    def close(self, new_close):
        self.__close = new_close

    @body.setter
    def body(self, new_body):
        self.__body = new_body

        ''' Opening and closing html elements '''
        # all code that will go in the <head></head> of the HTML doc + opening <body> tag
        self.__head = '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{self.title}</title>
                <link href='{self.css}' rel='stylesheet' />
            </head>
            <body>
        '''
        # closing tags to complete the html document
        self.__close = '''
            </body>
        </html>
        '''

        ''' Main content html elements '''
        # html blank body attribute to be filled later by the view class
        self.__body = ''

        self.__complete_page = (self.head + self.body + self.close)

forms_page = Page()
forms_page.body = '''
    <header>
        <h1>Price Checkr</h1>
    </header>
    <form method="get">
        <h2>Item Info</h2>
        <p class="input-field">
            <label for="item_name">Item Name</label>
            <input type="text" placeholder="item name" name="item_name">
        </p>
        <hr>
        <p class="input-field">
            <label for="original_price">Original Price <span class="glyph">$</span> </label>
            <input type="number" placeholder="Original price" name="original_price">
        </p>
        <hr>
        <p class="input-field">
            <label for="discount">Discount <span class="glyph">%</span> </label>
            <input type="number" placeholder="Discount" name="discount">
        </p>
        <hr>
        <p class="input-field">
            <label for="qty">Quantity <span class="glyph">#</span> </label>
            <input type="text" placeholder="qtyname" name="qty">
        </p>
        <hr>
        <input type="submit" value="submit" />
    </form>
'''
results_page = Page()
results_page.body = '''
    <header>
        <h2>Details</h2>
    </header>
    <div class ="details">
        <p> The {self.item_name} was originally priced at ${self.original_price}.The item's new price with the
        {discount}% discount is: </p>
        <p id ="discount_price">${discount_price}</p>
    </div>
'''

        if self.request.GET:
            self.results_body = self.results_body.format(**locals())
            self.response.write(self.__results_head + self.results_body +
                                self.results_close)
            self.response.write()
            self.head + self.body + self.close)
            self.all = self.all.format(**locals())






        ''' Final page output  '''

        '''
        # variable to concatenate html elements for page template
        self.page = ''
        # variable to concatenate all form page elements
        self.__form = ''
        # variable to concatenate results page elements
        self.__results = ''

        if self.request.GET:
            # store info from the form
            self.item_name = self.request.GET['item_name']
            self.original_price = self.request.GET['original_price']
            self.discount = self.request.GET['discount']
            self.qty = self.request.GET['qty']
            # form data submitted + stored in variables I can use to populate placeholders
            self.__results_body =
        < header >
        < h2 > Details / h2 >
        < / header >
        < div


        class ="details" >

        < p > The
        {self.item_name}
        was
        originally
        priced
        at ${self.original_price}.The
        item
        's new price with
        the
        {discount} % discount is: < / p >
        < p
        id = "discount_price" >${discount_price} < / p >
        < / div >

         # populate the placeholder content with data stored from the self.request.GET method
         self.results_body = self.results_body.format(**locals())
         # show page in browser with user data submitted via the form
         self.response.write(self.results_head + self.results_body + self.results_close)
        else:
         # otherwise show the page with a blank form
         self.response.write(self.form_head + self.form_body + self.form_close)


'''