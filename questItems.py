from items import Item

# A class to represent quest rewards, some containing special properties
class QuestItem(Item):

    # define a constructor
    # Name - the name of the item
    # Description - legend behind the item
    # Value - this item isn't tradeable
    # Enchantments - what properties does it have
    def __init__(self, name, description, value, enchantments):
        self.name = name
        self.description = description
        self.value = value
        self.enchantments = enchantments

    # Create a toString
    def __str__(self):
        return "\t{}\n======\n{}Name: {}   Value: {}   Description: {}    Enchantments: {}\n".format(self.name, self.value, self.description, self.enchantments)

class QuestWeapon(QuestItem):

    # Constructor
    def __init__(self, name, description, value, enchantments, damage):
        self.damage = damage
        super().__init__(name, description, value, enchantments)

    def __str__(self):
        return "\t{}\n======\n{}Name: {}   Value: {}   Description: {}    Enchantments: {}   Damage: {}\n".format(self.name, self.value, self.description, self.enchantments, self.damage)

    
