class Page(object):  # create a Page/abstract class as template for other pages
    def __init__(self):  # constructor function / turning it on
        # creating a few Master Page html elements to use on every page
        self._head = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Albert Martinez | Final Project | DPW-1606 WDDBS Full Sail University</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>

<body>
    <header id="header">
        <h1>Avatar: The Last Airbender</h1>
        <h2>Character Profiles</h2>
        <nav>
            <ul>
        '''
        # links for each of the individual characters' page
        self._links = '''
                <li><a href="?id=0">Aang</a></li>
                <li><a href="?id=1">Katara</a></li>
                <li><a href="?id=2">Sokka</a></li>
                <li><a href="?id=3">Toph</a></li>
                <li><a href="?id=4">Zuko</a></li>
        '''
        self._body = '''
            </ul>
        </nav>
    </header>
    <div id="details">
            <p class="intro">This site is made using Python to dynamically create web pages using Object-Oriented-Programming methods and ways, Python best practices, a smack load of research. and just a ramble of filler text for the time being.</br> Explore the mystical world of Avatar the last airbender characters and their profiles. Much of the description for Sokka, Toph, and Katara came from the awesome and incredible wiki page authors and contributors on their <a href="http://goo.gl/vlffPn" class="link inline">Avatar Wiki Page</a>
            </p>
    </div>
        '''
        self._close = '''
    </body>
</html>
        '''

    def print_it(self):  # method to print all master page parts of the html page
        return self._head + self._links + self._body + self._close


# make child page: inherits from Page class
class ContentPage(Page):
    """ VIEW """
    def __init__(self):  # constructor function / turning it on
        super(ContentPage, self).__init__()  # superclass constructor function
        # self.__character_list = []  # private array used to hold
        self._char_string = ''  # variable holding the character stats package sent from controller

    def print_it(self):
        return self._head + self._links + self._body + self._char_string + self._close
