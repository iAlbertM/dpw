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
            # if so, store the key:value in a variable
            character_id = int(self.request.GET['id'])
            # store the name of the character retrieved from characters array at index of character_id
            character_name = c.characters[character_id].name
            character_nation = c.characters[character_id].nation
            character_ability = c.characters[character_id].ability
            character_skill = c.characters[character_id].skill
            character_special = c.characters[character_id].special
            character_image = c.characters[character_id].image
            # check if character_id prints out the character that was clicked
            print(character_name)
            # if name == "Aang":
            # if true: load the characters stats into a list to send to the view
            # p.char_list.append(name, nation, ability, skill, special, image)
            self.response.write(p.print_it())
        else:
            self.response.write(p.print_it())
        self.response.write(p.print_it())


# class CharacterModel(object):
#     def __init__(self)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
# nation = 'Nation: ' + self.request.GET['nation']  # nation = c.characters[0].nation
# ability = 'Ability: ' + self.request.GET['ability']  # ability = c.characters[0].ability
# skill = 'Skill: ' + self.request.GET['skill']  # skill = c.characters[0].skill
# special = 'Special: ' + self.request.GET['special']  # special = c.characters[0].special
# image = 'Image: ' + self.request.GET['image']  # image = c.characters[0].image
# check if the data in request matches a characters name

# p.char_string = (name + nation + ability + skill + special + image)
# p.content = p.content.format(**locals())