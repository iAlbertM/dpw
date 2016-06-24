# the Parent Data class / abstract class: template for DataObjects
class Character(object):
    def __init__(self):
        self.name = ''
        self.nation = ''
        self.ability = ''
        self.skill = ''
        self.special = ''


# DataObject class: subclass with hardcoded data
class MainCharacter(Character):
    def __init__(self):  # initialising function for subclass
        super(MainCharacter, self).__init__()
        # aang - creating an instance of the Character class object
        aang = Character()
        aang.name = 'Aang'
        aang.nation = 'Air Nomads'
        aang.ability = 'Air Bender'
        aang.skill = 'Quick and Light on his feet'
        aang.special = 'the Avatar: bender of all elements'
        # katara - creating an instance of the Character class object
        katara = Character()
        katara.name = 'Katara'
        katara.nation = 'Southern Water Tribe'
        katara.ability = 'Water Bending'
        katara.skill = 'Healing & Blood Bending'
        katara.special = 'Waterbending Master & Teacher'
        # sokka - creating an instance of the Character class object
        sokka = Character()
        sokka.name = 'Sokka'
        sokka.nation = 'Southern Water Tribe'
        sokka.ability = 'Warrior'
        sokka.skill = 'Tactician & Swords Master'
        sokka.special = 'Chief of the Southern Water Tribe & the United Republic Council'
        # toph - creating an instance of the Character class object
        toph = Character()
        toph.name = 'Toph Beifong'
        toph.nation = 'Earth Kingdom'
        toph.ability = 'Earth Bender'
        toph.skill = 'Metalbender and blind but can "see" through vibrations in the earthl'
        toph.special = 'Earthbending Master & Teacher'
        # zuko - creating an instance of the Character class object
        zuko = Character()
        zuko.name = 'Zuko'
        zuko.nation = 'Fire Nation'
        zuko.ability = 'Fire Bender'
        zuko.skill = 'Redirect Lightning\nDual Dao swordsmanship'
        zuko.special = 'Prince Zuko / Fire Lord Zuko'

        self.characters = [aang, katara, sokka, toph, zuko]