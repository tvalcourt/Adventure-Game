import items

# abstract base enchantment
class Enchantment():

    # Element
    # Extra Damage
    # Prefix
    def __init__(self, element, damage, prefix):
        self.element = element
        self.damage = damage
        self.prefix = prefix

    # self = Player
    # item = best_weapon
    def apply_enchantment(self, item):
        item.name = "Flaming " + item.name
        #item.damage += FireEnchantment().damage

    def is_enchanted(self, item):
        return item.enchanted == 1


# Create a few basic enchantments
class FireEnchantment(Enchantment):

    def __init__(self):
        super().__init__(element='Fire',
                         damage=10,
                         prefix="Flaming")
        
    # self = Player
    # item = best_weapon
    def apply_enchantment(self, item):
        item.name = "Flaming " + item.name
        item.damage += FireEnchantment().damage
    
