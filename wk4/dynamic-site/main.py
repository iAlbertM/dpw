import webapp2
from data import CharacterData
from pages import ContentPage

# Avatar fans can look up stats about their favorite good main character from the show:
# Avatar the Last Airbender by clicking on the name of that character it loads their page
# CONTROLLER: handles retrieving of all data from character database
# data from database will be added to an array
# array will be used to concatenate: data + <html></elements> to send to view
class MainHandler(webapp2.RequestHandler):
    """ CONTROLLER """
    def get(self):
        p = ContentPage()  # creates an instance of ContentPage class object
        c = CharacterData()  # creates an instance of the characters list from database
        if self.request.GET:  # check if there are any variables in the URL
            # if there are, create variables to hold the specific information within the request
            name = 'Name: ' + self.request.GET['name']  # name = ('c.' + c.characters[0] + '.name')
            nation = 'Nation: ' + self.request.GET['nation']  # nation = c.characters[0].nation
            ability = 'Ability: ' + self.request.GET['ability']  # ability = c.characters[0].ability
            skill = 'Skill: ' + self.request.GET['skill']  # skill = c.characters[0].skill
            special = 'Special: ' + self.request.GET['special']  # special = c.characters[0].special
            image = 'Image: ' + self.request.GET['image']  # image = c.characters[0].image
            # check if the data in request matches a characters name
            if name == "Aang":

                # if true: load the characters stats into a list to send to the view
                p.char_list.append(name, nation, ability, skill, special, image)
            # p.char_string = (name + nation + ability + skill + special + image)
            # p.content = p.content.format(**locals())
            self.response.write(self.request.Get)
        else:
            self.response.write(p.print_it())
        self.response.write(p.print_it())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
