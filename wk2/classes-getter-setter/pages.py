class Page(object):
    def __init__(self):
        self.__title = 'Welcome!'
        self.__css = 'css/main.css'
        self.head = '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{self.title}</title>
                <link href='{self.css}' rel='stylesheet' />
            </head>
            <body>
        '''
        self.__body = 'Welcome to my OOP Python page!'
        self.close = '''
            </body>
        </html>
        '''
        self.whole_page =""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()


    @property
    def css(self):
        return self.__css


    @css.setter
    def css(self, new_css):
        self.__css = new_css
        self.update()