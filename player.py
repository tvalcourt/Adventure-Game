import random,items,world,enchantments
from enchantments import FireEnchantment, Enchantment

class Player:
    inventory = [items.Gold(15), items.Rock()]
    health = 100
    location_x, location_y = (2,4)
    victory = False

    def is_alive(self):
        return self.health > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    # add actions to make the player move around
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


    # Our hero must be able to fight!
    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0

        # find best equipment
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use your {} against the {}!".format(best_weapon.name, enemy.name))
        enemy.health -= best_weapon.damage

        # If you slay the enemy
        if not enemy.is_alive():
            print("You killed the {}!".format(enemy.name))
        else:
            print("The {} has {} HP remaining!".format(enemy.name, enemy.health))

    # Our hero can apply enchantments if he has a stone
    # The current implementation makes it so the hero applies it only to the
    # best weapon that the hero has. (But come on, why wouldn't you?)
    def enchant(self):

        best_weapon = None
        max_dmg = 0

        # first check if the hero has a stone
        for item in self.inventory:
            if isinstance(item, items.FireStone):
                
                # Remove the item from the player's inventory
                self.inventory.remove(item)

                # Now find the best weapon
                for i in self.inventory:
                    if isinstance(i, items.Weapon):
                        if i.damage > max_dmg:
                            best_weapon = i
                            
                if Enchantment.is_enchanted(self, best_weapon):
                    return "Your best weapon is already enchanted. You foolisly bresk your stone in the process"
                else:
                    # Now apply the enchantment
                    FireEnchantment.apply_enchantment(self, best_weapon)

                
                            

    # Moves the player randomly to an adjacent tile
    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) -1)
        self.do_action(available_moves[r])

    # completes the given action
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)

        if action_method:
            action_method(**kwargs)












        
