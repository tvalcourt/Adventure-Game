class Item():
    #a base class for any and all items

    #define a Constructor
    #Name - The name of the item
    #Description - What does the item do
    #Value - Some form of monetary value assigned to it
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    #Think of this like a toString method in Java
    def __str__(self):
        return "{}\n=====\n{}Value: {}\n".format(self.name, self.description, self.value)

# Items to apply enchantments
class FireStone(Item):

    def __init__(self):
        super().__init__(name="Fire Stone\t",
                         description="Applies a fire enchantment to a weapon\t",
                         value=150)

# class gold extends item
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

# define a class of generic class of weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage, enchanted):
        self.damage = damage
        self.enchanted = enchanted
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}Value: {}   Damage: {}\n".format(self.name, self.description, self.value, self.damage)

# define a few different weapons
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A basic Dagger. Nothing special here.",
                         value=10,
                         damage=10,
                         enchanted=0)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A pretty average Rock. Can serve as a potent weapon.",
                         value=0,
                         damage=5,
                         enchanted=0)

