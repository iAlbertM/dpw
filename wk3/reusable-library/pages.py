class Page(object):  # create a page class to store all HTML + CSS code
    def __init__(self):  # initialize the Page class
        self.__title = ''  # create a private property to hold: title of html document
        self.__css = ''  # create a private property to hold: path to css stylesheet
        self.__js = ''  # create a private property to hold: path to js file
        self.__page_template = ''  # a page template property holding all other properties of the Page class

        # all code that will go in the <head></head> of the HTML doc + opening <body> tag
        self.__head = ''''''
        # all code that will be rendred by the browser and visible to user
        self.__body = ''''''
        # closing tags to complete the html document
        self.__close = ''''''

