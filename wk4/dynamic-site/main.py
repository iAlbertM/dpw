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
        character_stats_model = ''  # use to package the character stats for the view
        if self.request.GET:  # check if there are any variables in the URL
            # if so, store the key:value in a variable to use it later when retrieving info from CharacterData class
            character_id = int(self.request.GET['id'])

            # RETRIEVE DATA: from CharacterData class based on information from request.GET
            # STORE: each stat into its own variable so that it can be more easily accessible
            character_name = c.characters[character_id].name
            character_nation = c.characters[character_id].nation
            character_ability = c.characters[character_id].ability
            character_skill = c.characters[character_id].skill
            character_official = c.characters[character_id].official
            character_image = c.characters[character_id].image
            character_description = c.characters[character_id].description

            # QUICK STATUS CHECK CODE  -- NOT NEEDED FOR APP TO RUN JUST A CHECKPOINT TO ENSURE IT WAS WORKING AT ALL
            #   print(character_name)  #   check if character_id prints out the character that was clicked
            # PACKAGING DATA RETREIVED FROM DATABASE: package the stats to send to the view
            p.body = '''<div id="details">\n\t'''
            p.body += '<h3 class="label">Description: \t</h3>\n<p>' + character_description + '</p>\n</div>\n'

            # creating the Character Stats section for each page concatenating the values from the request + html tags
            character_stats_model += '<div class="character-image">\n'  # creating a div for the image - styling purposes
            character_stats_model += '\t<img src="' + character_image + '" alt="Photo of ' + character_name + '"> \n</div>'  # character photo with src and alt attributes
            character_stats_model += '<div id="' + character_name + '-stats\">\n'  # div to hold each characters' stats
            character_stats_model += '  <p class="stats"><span class="label">Name: </span>' + character_name + '</p>\n'  # character name
            character_stats_model += '  <p class="stats"><span class="label">Nation: </span> ' + character_nation + '</p>\n'  # character's nationality/race
            character_stats_model += '  <p class="stats"><span class="label">Ability:  </span> ' + character_ability + '</p>\n' # a special ability they possess
            character_stats_model += '  <p class="stats"><span class="label">Skill:  </span> ' + character_skill + '</p>\n'  # A special skill they developed throughout the show
            character_stats_model += '  <p class="stats"><span class="label">Title(s):  </span> ' + character_official + '</p>\n'  #titles, awareds, or acheivements they receiveed throughout the show
            character_stats_model += '</div>\n'  # div to hold each characters' stats
            p._char_string = character_stats_model

            # if true: load the characters stats into a list to send to the view
            # p.char_list.append(name, nation, ability, skill, official, image)
            self.response.write(p.print_it())
        else:
            self.response.write(p.print_it())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
