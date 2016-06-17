class Page(object):  # creating Page class to serve as template for other pages
    def __init__(self):  # initializing Page class
        # setting default values for Page class attributes
        # all code that will go in the <head></head> of the HTML doc
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
        # html blank body attribute to be filled later by the form or result attr.
        self.__body = ''

        # the form body and form html elements
        self.__form = '''
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
                <p class="input-field"><label for="original_price">
                Original Price <span class="glyph">$</span></label>
                    <input type="number" placeholder="Original price"
                    name="original_price">
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
        # defining the result body contents attribute
        self.__result = '''
        <header>
            <h2>Details</h2>
        </header>
        <div class ="details">
            <p> The {self.item_name} was originally priced at ${self.original_price}.The item's new price with the
            {discount}% discount is: </p>
            <p id ="discount_price">${discount_price}</p>
        </div>
        '''
        self.__title = 'My Title'  # private property to hold: html title
        self.__css = 'css/main.css'  # private property to hold: path to css file
        self.__js = 'js/main.js'  # private property to hold: path to js file
        self.__complete_page = (self.head + self.body + self.close)
        self.__form_page = (self.head + self.body + self.form + self.close)
        self.__result_page = (self.head + self.body + self.result + self.close)

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

    @property
    def form(self):
        return self.__form

    @property
    def result(self):
        return self.__result

    @property
    def form_page(self):
        return self.__form_page

    @property
    def result_page(self):
        return self.__result_page

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

    @complete_page.setter
    def complete_page(self, new_complete_page):
        self.__complete_page = new_complete_page

    @form.setter
    def form(self, new_form):
        self.__form = new_form

    @result.setter
    def result(self, new_result):
        self.__result = new_result

    @form_page.setter
    def form_page(self, new_form_page):
        self.__form_page = new_form_page

    @result_page.setter
    def result_page(self, new_result_page):
        self.__result_page = new_result_page
