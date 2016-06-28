###########

# author/creator: Albert Martinez
# project: Website created dynamically with Python
# course: DPW Design Patterns for Web Programming 1606
# instructor: Rebecca Carroll

###########
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
        self.description = ''


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
        aang.image = 'img/aang.png'
        aang.description = 'Aang is the fun-loving, 112-year-old protagonist of the series, who is biologically twelve years old but was frozen in an iceberg for one hundred years. He is the current incarnation of the Avatar, the spirit of the world manifested into human form, whose duty is to maintain balance among the nations of the world. Aang is a reluctant hero, who would prefer adventure over his job as the Avatar and making friends over fighting the Fire Nation.'  # Source: Avatar: The Last Airbender. (2016). Avatar Wiki. Retrieved from http://avatar.wikia.com/wiki/Avatar:_The_Last_Airbender
        # katara - creating an instance of the Character class object
        katara = Character()
        katara.name = 'Katara'
        katara.nation = 'Southern Water Tribe'
        katara.ability = 'Waterbender'
        katara.skill = 'Healing & Blood Bending'
        katara.official = 'Waterbending Master & Teacher'
        katara.image = 'img/katara.png'
        katara.description = ''' Katara is a fourteen-year-old female waterbender of the Southern Water Tribe, the only waterbender in the tribe. Katara discovers and frees Aang from an iceberg in which he had been trapped for a hundred years. With her fifteen-year-old brother Sokka, she accompanies Aang on his quest to defeat the Fire Lord and bring peace to the world. In the original unaired pilot episode, Katara's name was Kya; this later used as her mother's name.'''  # Source: Avatar: The Last Airbender. (2016). Avatar Wiki. Retrieved from http://avatar.wikia.com/wiki/Avatar:_The_Last_Airbender

        # sokka - creating an instance of the Character class object
        sokka = Character()
        sokka.name = 'Sokka'
        sokka.nation = 'Southern Water Tribe'
        sokka.ability = 'Warrior'
        sokka.skill = 'Tactician & Swords Master'
        sokka.official = 'Chief of the Southern Water Tribe & the United Republic Council'
        sokka.image = 'img/sokka.png'
        sokka.description = 'Sokka is a fifteen-year-old warrior of the Southern Water Tribe. With his sister Katara, he accompanies Aang on his quest to defeat the Fire Lord. The joker of the group, Sokka describes himself as \"meat-loving\" and \"sarcastic\". Unlike his companions, Sokka cannot bend an element, but the series, though it often makes him the victim of comedy at his expense, frequently grants him opportunities to use his ingenuity and weapons, including his trusty boomerang and a sword he forged from a meteorite.' # Source: Avatar: The Last Airbender. (2016). Avatar Wiki. Retrieved from http://avatar.wikia.com/wiki/Avatar:_The_Last_Airbender

        # toph - creating an instance of the Character class object
        toph = Character()
        toph.name = 'Toph'
        toph.nation = 'Earth Kingdom'
        toph.ability = 'Earthbender'
        toph.skill = 'Metalbender and blind but can "see" through vibrations in the earthl'
        toph.official = 'Earthbending Master & Teacher'
        toph.image = 'img/toph.png'
        toph.description = '''Toph is a fifteen-year-old warrior of the Southern Water Tribe. With his sister Katara, he accompanies Aang on his quest to defeat the Fire Lord. The joker of the group, Sokka describes himself as "meat-loving" and "sarcastic". Unlike his companions, Sokka cannot bend an element, but the series, though it often makes him the victim of comedy at his expense, frequently grants him opportunities to use his ingenuity and weapons, including his trusty boomerang and a sword he forged from a meteorite.'''  # Source: Avatar: The Last Airbender. (2016). Avatar Wiki. Retrieved from http://avatar.wikia.com/wiki/Avatar:_The_Last_Airbender

        # zuko - creating an instance of the Character class object
        zuko = Character()
        zuko.name = 'Zuko'
        zuko.nation = 'Fire Nation'
        zuko.ability = 'Firebender'
        zuko.skill = 'Redirect Lightning\nDual Dao swordsmanship'
        zuko.official = 'Prince Zuko / Fire Lord Zuko'
        zuko.image = 'img/zuko.png'
        zuko.description = '''Zuko is the sixteen-year-old exiled prince of the Fire Nation and original antagonist of the series. Due to events in Zuko's past, his father, Fire Lord Ozai, deems him a complete failure, and Zuko feels he must capture the Avatar to regain his honor. Over time, Zuko struggles to deal with his anger, self-pity, and familial relationships; meanwhile, he grows sympathetic to the peoples his nation has terrorized. In Book Three, he defects from the Fire Nation and joins Aang and the team in order to teach Aang firebending. At the end of the series, he is crowned ruler of the Fire Nation.'''  # Source: Avatar: The Last Airbender. (2016). Avatar Wiki. Retrieved from http://avatar.wikia.com/wiki/Avatar:_The_Last_Airbender


        self.characters = [aang, katara, sokka, toph, zuko]
