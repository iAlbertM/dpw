# DataObject Class: Template used to create like-objects in other classes
class Character(object):
    def __init__(self):  # turn object on
        # default attributes for this object's instances
        self.name = ''
        self.nation = ''
        self.ability = ''
        self.skill = ''
        self.special = ''
        self.image = ''


# Data Class - store all DataObjects to simulate a database
class CharacterData(object):
    """ CHARACTER DATABASE """
    def __init__(self):  # initialize-turn on
        # aang - creating an instance of the Character class object
        aang = Character()
        aang.name = 'Aang'
        aang.nation = 'Air Nomads'
        aang.ability = 'Airbender'
        aang.skill = 'Avatar State'
        aang.official = 'the Avatar: bender of all elements'
        aang.image = 'img/aang.jpg'
        # katara - creating an instance of the Character class object
        katara = Character()
        katara.name = 'Katara'
        katara.nation = 'Southern Water Tribe'
        katara.ability = 'Waterbender'
        katara.skill = 'Healing & Blood Bending'
        katara.official = 'Waterbending Master & Teacher'
        katara.image = 'img/katara.jpg'
        # sokka - creating an instance of the Character class object
        sokka = Character()
        sokka.name = 'Sokka'
        sokka.nation = 'Southern Water Tribe'
        sokka.ability = 'Warrior'
        sokka.skill = 'Tactician & Swords Master'
        sokka.official = 'Chief of the Southern Water Tribe & the United Republic Council'
        sokka.image = 'img/sokka.jpg'
        # toph - creating an instance of the Character class object
        toph = Character()
        toph.name = 'Toph Beifong'
        toph.nation = 'Earth Kingdom'
        toph.ability = 'Earthbender'
        toph.skill = 'Metalbender and blind but can "see" through vibrations in the earthl'
        toph.official = 'Earthbending Master & Teacher'
        toph.image = 'img/toph.jpg'
        # zuko - creating an instance of the Character class object
        zuko = Character()
        zuko.name = 'Zuko'
        zuko.nation = 'Fire Nation'
        zuko.ability = 'Firebender'
        zuko.skill = 'Redirect Lightning\nDual Dao swordsmanship'
        zuko.official = 'Prince Zuko / Fire Lord Zuko'
        zuko.image = 'img/zuko.jpg'

        self.characters = [aang, katara, sokka, toph, zuko]
