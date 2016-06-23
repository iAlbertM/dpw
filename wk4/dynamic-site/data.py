# the Data class / abstract class: template for DataObjects
class Character(object):
    def __init__(self):
        self.name = ''
        self.nation = ''
        self.ability = ''
        self.skill = ''
        self.special = ''
        self.description = ''


# DataObject class: subclass of the super/parant class Character
class AvatarCharacter(Character):
    def __init_(self): # initialising function
        # invoking the constructor function of parent class
        super(AvatarCharacter, self).__init_()

        # aang - creating an instance of the AvatarCharacter class object
        aang = AvatarCharacter()
        aang.name = 'Aang'
        aang.nation = 'Air Nomads'
        aang.ability = 'Air Bender'
        aang.skill = 'Quick and Light on his feet'
        aang.special = 'the Avatar: bender of all elements'
        aang.description = '''Aang is the only survivor from the raid of the Fire Nation's surprise attack on the Air Nation. Aang's destiny is to master all 4 elements and as the only hope to bring balance, harmony, and peace to the world.'''

        # katara - creating an instance of the AvatarCharacter class object
        katara = AvatarCharacter()
        katara.name = 'Katara'
        katara.nation = 'Southern Water Tribe'
        katara.ability = 'Water Bending'
        katara.skill = 'Healing & Blood Bending'
        katara.special = 'Waterbending Master & Teacher'
        katara.description = '''Katara is a waterbending master, born in the Southern Water Tribe to Chief Hakoda and his wife, Kya. During her childhood, she was the only waterbender living in the South Pole. At first she lived a peaceful life with her family, until she lost her mother in a Fire Nation raid. After her father left to battle against the Fire Nation in the Hundred Year War, Katara was raised by her grandmother, Kanna, alongside her older brother Sokka. As a teenager, she and her brother discovered the young Air Nomad Avatar, Aang, who had been frozen in an iceberg with his bison, Appa, for one hundred years. In need of a waterbending master, the siblings and Aang left the South Pole on a journey toward the Northern Water Tribe. Katara and Sokka eventually became close friends with Aang, and after their journey to the North Pole, continued to travel with him across the world as he mastered the remaining elements, earth and fire. The siblings' assistance helped Aang halt the Fire Nation's ambitions of world domination, ending the century-long war, and finally restoring balance to the world.''' # Source: Katara. (2016). Avatar Wiki. Retrieved 23 June 2016, from http://avatar.wikia.com/wiki/Katara

        # sokka - creating an instance of the AvatarCharacter class object
        sokka = AvatarCharacter()
        sokka.name = 'Sokka'
        sokka.nation = 'Southern Water Tribe'
        sokka.ability = 'Warrior'
        sokka.skill = 'Tactician & Swords Master'
        sokka.special = 'Chief of the Southern Water Tribe & the United Republic Council'
        sokka.description = '''Sokka was a Water Tribe warrior of the Southern Water Tribe and the son of Chief Hakoda and Kya. Following the death of his mother and his father's leave for war, Sokka was raised by his grandmother Kanna along with his younger sister Katara.
Hakoda left along with all of the other men in his tribe to fight the Fire Nation when Sokka was a young boy. Despite his desire to join his father, Sokka was not permitted to accompany the men on the mission and was left behind. As there were no other teenage boys in the tribe, Sokka was the oldest male in the South Pole and, therefore, left as the leader of the tribe. He assumed responsibility for the tribe, haplessly training children to be future warriors, until his sister discovered an Air Nomad named Aang frozen in an iceberg. When he learned that Aang was the Avatar, he was at first skeptical that a child could really save the world. As he and his sister helped Aang on his quest, he began to believe that Aang really was the only hope for peace in the world.''' # Sokka. (2016). Avatar Wiki. Retrieved 23 June 2016, from http://avatar.wikia.com/wiki/Sokka

        # toph - creating an instance of the AvatarCharacter class object
        toph = AvatarCharacter()
        toph.name = 'Toph Beifong'
        toph.nation = 'Earth Kingdom'
        toph.ability = 'Earth Bender'
        toph.skill = 'Metal Bender and Vibrational Sight (blind but can "see" through vibrations in the earth'
        toph.special = 'Earthbending Master & Teacher'
        toph.description = '''Toph Beifong is an earthbending master, one of the most powerful of her time, and the discoverer of metalbending. Blind since birth, Toph was constantly treated condescendingly because of her blindness, particularly by her overprotective parents, Lao and Poppy Beifong. Having developed her own unique style of earthbending, Toph acquired a toughened personality and became famous for winning underground earthbending tournaments under the name "The Blind Bandit" Toph eventually chose to leave behind her old life, and travel with Avatar Aang and his friends as his earthbending teacher.''' # Source: Toph Beifong. (2016). Avatar Wiki. Retrieved 23 June 2016, from http://avatar.wikia.com/wiki/Toph_Beifong

        # zuko - creating an instance of the AvatarCharacter class object
        zuko = AvatarCharacter()
        zuko.name = 'Zuko'
        zuko.nation = 'Fire Nation'
        zuko.ability = 'Fire Bender'
        zuko.skill = 'Redirect Lightning\nDual Dao swordsmanship'
        zuko.special = 'Prince Zuko / Fire Lord Zuko'
        zuko.description = '''Zuko, a.k.a. Prince Zuko, son of Fire Lord Ozai and Princess Ursa (went missing before Prince Ozai became firelord). After an outburst during a meeeting with the Generals of the Fire Nation, Zuko was exiled only to return with the avatar who had been missing for 100 years. Zuko started off hunting the avatar, only to later join his team and his journey to bring harmony to the world.'''
