class Page(object):
    def __init__(self):
        self.title = 'Welcome!'
        self.css = 'css/main.css'
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
        self.body = 'Welcome to my OOP Python page!'
        self.close = '''
            </body>
        </html>
        '''

    def print_out(self):
        elem = self.head + self.body + self.close
        elem = elem.format(**locals())
        return elem
