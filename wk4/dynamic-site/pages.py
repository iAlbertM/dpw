class Page(object):
    def __init__(self):
        self._head = '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Albert Martinez | {self.title} WDDBS Full Sail University</title>
                <link rel="stylesheet" type="text/css" href="css/main.css">
            </head>
            <body>
        '''
        self._body = "Hola World!"
        self._close = '''
            </body>
        </html>
        '''

    def print_page(self):
        return self._head + self._body + self._close

class ContentPage(Page):
    def __init__(self):
        def super(FormPage, self).__init__()
        self._body = '''

        '''

