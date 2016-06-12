class ResultsPage(object):
    def __init__(self):
        self.__title = 'welcome!'
        self.css = 'css/styles.css'
        self.__head = '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset='utf-8'>
                <title>Albert Martinez | Reusable Library | DPW-1606</title>
            </head>
            <body>
        '''

        self.body = ''
        self.__error = ''
        self.__close = '''
            </body>
        </html>
        '''

    def print_out(self):
        all = self.__head + self.body + self.__error + __self.__close
        return all
