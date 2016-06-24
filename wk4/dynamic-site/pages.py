class Page(object):
    def __init__(self):
        self._title = ''
        self._head = '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Albert Martinez | {self.title} WDDBS Full Sail University</title>
                <link rel="stylesheet" type="text/css" href="css/main.css">
            </head>
            <body>
                <header>
                    <h1>Avatar: The Last Airbender</h1>
                    <h2>{c.name}</h2>
                    <nav>
                        <ul>
                            <li><a href="?name=Aang">Aang</a></li>
                            <li><a href="?name=Katara">Katara</a></li>
                            <li><a href="?name=Sokka">Sokka</a></li>
                            <li><a href="?name=Toph">Toph</a></li>
                            <li><a href="?name=Zuko">Zuko</a></li>
                        </ul>
                    </nav>
                </header>
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
        super(ContentPage, self).__init__()
        self._body = '''

        <div id="details">

        </div>

        '''

