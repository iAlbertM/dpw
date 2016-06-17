class FormPage(object):  # create a page class to store all HTML + CSS code
    def __init__(self):  # initialize the Page class
        self.__title = 'My Title'  # create a private property to hold: title of html document
        self.__css = 'css/main.css'  # create a private property to hold: path to css stylesheet
        self.__js = 'js/main.js'  # create a private property to hold: path to js file

        @property
        def form_title(self):
            return self.__form_title

        @property
        def form_css(self):
            return self.__form_css

        @property
        def js(self):
            return self.__js

        @property
        def form_head(self):
            return self.__form_head

        @property
        def form_close(self):
            return self.__form_close

        @property
        def form_body(self):
            return self.__form_body

        @form_title.setter
        def form_title(self, new_form_title):
            self.__form_title = new_form_title

        @form_css.setter
        def form_css(self, new_form_css):
            self.__form_css = new_form_css

        @js.setter
        def js(self, new_js):
            self.__js = new_js

        @form_head.setter
        def form_head(self, new_form_head):
            self.__form_head = new_form_head

        @form_close.setter
        def form_close(self, new_form_close):
            self.__form_close = new_form_close

        @form_body.setter
        def form_body(self, new_form_body):
            self.__form_body = new_form_body

        ''' Opening and closing html elements '''
        # all code that will go in the <head></head> of the HTML doc + opening <body> tag
        self.__form_head = '''
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
        self.__form_close = '''
            </body>
        </html>
        '''

        ''' Main content html elements '''
        # html form page html
        self.__form_body = '''
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

class ResultsPage(object):  # create a page class to store all HTML + CSS code
    def __init__(self):  # initialize the Page class
        self.__results_title = 'My Title'  # create a private property to hold: title of html document
        self.__results_css = ''  # create a private property to hold: path to css stylesheet

        @property
        def results_title(self):
            return self.__results_title

        @property
        def results_css(self):
            return self.__results_css
        @property
        def results_head(self):
            return self.__results_head

        @property
        def results_close(self):
            return self.__results_close

        @property
        def results_body(self):
            return self.__results_body

        @results_title.setter
        def results_title(self, new_results_title):
            self.__results_title = new_results_title

        @results_css.setter
        def results_css(self, new_results_css):
            self.__results_css = new_results_css

        @results_head.setter
        def results_head(self, new_results_head):
            self.__results_head = new_results_head

        @results_close.setter
        def results_close(self, new_results_close):
            self.__results_close = new_results_close

        @results_body.setter
        def results_body(self, new_results_body):
            self.__results_body = new_results_body



        ''' Opening and closing html elements '''
        # all code that will go in the <head></head> of the HTML doc + opening <body> tag
        self.__results_head = '''
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
        self.__results_close = '''
            </body>
        </html>
        '''

        # html results page html
        self.__results_body = '''
        <header>
            <h2>Details</h2>
        </header>
        <div class ="details">
            <p> The {self.item_name} was originally priced at ${self.original_price}.The item's new price with the
            {discount}% discount is: </p>
            <p id ="discount_price">${discount_price}</p>
        </div>
        '''

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