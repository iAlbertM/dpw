class FormPage(object):  # create a page class to store all HTML + CSS code
    def __init__(self):  # initialize the Page class
        self.__title = 'My Title'  # create a private property to hold: title of html document
        self.__css = 'css/main.css'  # create a private property to hold: path to css stylesheet
        self.__js = 'js/main.js'  # create a private property to hold: path to js file

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
        def form_body(self):
            return self.__form_body

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

        @form_body.setter
        def form_body(self, new_form_body):
            self.__form_body = new_form_body

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
        self.__title = 'My Title'  # create a private property to hold: title of html document
        self.__css = ''  # create a private property to hold: path to css stylesheet
        self.__js = ''  # create a private property to hold: path to js file

        @property
        def title(self):
            return self.__title

        @property
        def css(self):
            return self.__css
        @property
        def head(self):
            return self.__head

        @property
        def close(self):
            return self.__close

        @property
        def results_body(self):
            return self.__results_body

        @title.setter
        def title(self, new_title):
            self.__title = new_title

        @css.setter
        def css(self, new_css):
            self.__css = new_css

        @head.setter
        def head(self, new_head):
            self.__head = new_head

        @close.setter
        def close(self, new_close):
            self.__close = new_close

        @results_body.setter
        def results_body(self, new_results_body):
            self.__results_body = new_results_body



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
        # variable to concatenate html elements for page template
        self.__page_template = ''
        # variable to concatenate all form page elements
        self.__form = ''
        # variable to concatenate results page elements
        self.__results = ''