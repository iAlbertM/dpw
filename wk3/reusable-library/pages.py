class Page(object):  # create a page class to store all HTML + CSS code
    def __init__(self):  # initialize the Page class
        self.__title = ''  # create a private property to hold: title of html document
        self.__css = ''  # create a private property to hold: path to css stylesheet
        self.__js = ''  # create a private property to hold: path to js file

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
        self.close = '''
            </body>
        </html>
        '''

        ''' Main content html elements '''
        # all scode that will be rendred by the browser and visible to user
        self.body = ''''''
        # html form page html
        self.form_body = '''
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
        # html results page html
        self.results_body = '''
        
        '''

        ''' Final page output  '''
        # variable to concatenate html elements for page template
        self.__page_template = ''
        # variable to concatenate all form page elements
        self.__form = ''
        # variable to concatenate results page elements
        self.__results = ''