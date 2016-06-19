# first page view class: FormPage
class FormPage(object):
    # initializing Page class
    def __init__(self):
        # private property to hold: path to css file
        self.__css = 'css/main.css'

        # all code that will go in the <head></head> of the HTML doc
        self.__head = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
                <meta charset="UTF-8">
                <title>"Albert Martinez | Reusable Library | DPW-1606 WDDBS Full Sail University"</title>
                <link href={self.css}; rel='stylesheet' />
        </head>
        <body>
        '''
        
        # html blank body attribute to be filled later by the form or result attr.
        self.__body = '''
            <header>
                <h1>PriceCheckr</h1>
            </header>
            <form method="get">
                <h2>Item Info</h2>
                <p class="input-field">
                    <label for="item">Item Name</label>
                    <input type="text" placeholder="Item" name="item">
                </p>
                <hr>
                <p class="input-field"><label for="price"> Price $ </label>
                    <input type="number" placeholder="Price" name="price">
                </p>
                <hr>
                <p class="input-field">
                    <label for="discount">Discount % </label>
                    <input type="number" placeholder="Discount" name="discount">
                </p>
                <hr>
                <p class="input-field">
                    <label for="qty">Quantity # </label>
                    <input type="number" placeholder="Qty" name="qty">
                </p>
                <hr>
                <input type="submit" value="submit" />
            </form>
        '''
      
        # closing tags to complete the html document
        self.__close = '''
        </body>
        </html>
        '''

    @property
    def css(self):
        return self.__css
    
    @css.setter
    def css(self, new_css):
        self.__css = new_css

    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self, new_head):
        self.__head = new_head

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body

    @property
    def close(self):
        return self.__close

    @close.setter
    def close(self, new_close):
        self.__close = new_close

    def print_page(self):
        all = self.__head + self.__body + self.__close
        return all


# second page view class: ResultPage
class ResultPage(object):
    # initializing Page class
    def __init__(self):
        self.__title = 'Albert Martinez | Reusable Library: Results Page'
        # private property to hold: path to css file
        self.__css = 'css/main.css'
        # all code that will go in the <head></head> of the HTML doc
        self.__head = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
                <meta charset="UTF-8">
                <title>{self.title}</title>
                <link href={self.css}; rel='stylesheet' />
        </head>
        <body>
        '''

        # html blank body attribute to be filled later by the form or result attr.
        self.__body = ''

        # closing tags to complete the html document
        self.__close = '''
        </body>
        </html>
        '''
        self.complete = ""

    # def build_page(self):
    #     self.complete = self.head + self.body + self.close
    #     self.complete = self.complete.format(**locals())

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css):
        self.__css = new_css

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, new_head):
        self.__head = new_head

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.print_page()
    @property
    def close(self):
        return self.__close

    @close.setter
    def close(self, new_close):
        self.__close = new_close

    def print_page(self):
        all = self.__head + self.__body + self.__close
        all = all.format(**locals())
        return all
