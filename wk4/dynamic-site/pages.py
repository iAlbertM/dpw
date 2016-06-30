###########

# author/creator: Albert Martinez
# project: Website created dynamically with Python
# course: DPW Design Patterns for Web Programming 1606
# instructor: Rebecca Carroll

###########

class Page(object):  # create a Page/abstract class as template for other pages
    def __init__(self):  # constructor function / turning it on
        # creating a few Master Page html elements to use on every page
        self._head = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Albert Martinez | Final Project | DPW-1606 WDDBS Full Sail University</title>

    <link href="https://fonts.googleapis.com/css?family=Acme" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/main.css">

</head>
<body>
    '''
        # links for each of the individual characters' page
        self._nav = ''' <header id="header">
        <h1>Avatar: The Last Airbender</h1>
        <h2>Character Profiles</h2>
        <nav>
            <ul>
                <li><a href="?id=0">Aang</a></li>
                <li><a href="?id=1">Katara</a></li>
                <li><a href="?id=2">Sokka</a></li>
                <li><a href="?id=3">Toph</a></li>
                <li><a href="?id=4">Zuko</a></li>
            </ul>
        </nav>
    </header>
        '''
        self._body = '''
                    <p class="intro">This is the Avatar mini Character Profiles Site. Here you can find out a little bit about your favorite good main characters from the show Avatar: The Last Airbender. If you never heard of this show here's a brief description straight from the Avatar Wiki Parent Page:</p>\n<p<The human civilization is divided into four, though eventually five, nations: the Water Tribes, the Earth Kingdom, the Air Nomads, the Fire Nation, and the United Republic of Nations. Each nation has its own natural element, on which it bases its society, and within each nation exist people known as "benders" who have the innate power and ability to control and manipulate, or "bend", the eponymous element of their nation. Each generation yields one person who is capable of controlling and manipulating all four elements, the Avatar, whose job it is to keep the four nations in harmony, and maintain world peace and order.</p>\n<p>Explore the mystical world of Avatar the last airbender characters and their profiles. Much of the description for Sokka, Toph, and Katara came from the awesome and incredible wiki page authors and contributors on their <a href="http://goo.gl/vlffPn" class="link inline">Avatar Wiki Page</a>
                    </p>
        '''
        self._close = '''<footer>
    <p>This site uses material from the <a href="http://avatar.wikia.com/wiki/Avatar:_The_Last_Airbender" class="link inline">"Avatar: The Last Airbender" wiki</a> at Wikia and is licensed under the <a href="http://wikia.com/Licensing" class="link inline">Creative Commons Attribution-Share Alike License 3.0 (Unported) (CC-BY-SA)</a>.</p
    </footer>
</body>
</html>
        '''
    @property # define a getter for self._body to be retrieved from outside this class- read access
    def body(self):
        return self._body

    @body.setter  # define a setter for self._body to allow write access to body
    def body(self, new_body):
        self._body = new_body

    def print_it(self):  # method to print all master page parts of the html page
        return self._head + self._nav + self._body + self._close


# make child page: inherits from Page class
class ContentPage(Page):
    """ VIEW """
    def __init__(self):  # constructor function / turning it on
        super(ContentPage, self).__init__()  # superclass constructor function
        self._char_string = ''  # variable holding the character stats package sent from controller

    @property  # define a getter for self._body to be retrieved from outside this class- read access
    def char_string(self):
        return self._char_string

    @char_string.setter  # define a setter for self._body to allow write access to body
    def char_string(self, new_string):
        self._char_string = new_string


    def print_it(self):
        return self._head + self._nav + self._char_string + self._body  + self._close
