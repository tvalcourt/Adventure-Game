from player import Player

# Abstract to define an action
class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


# Hotkey actions for movement
class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name ="Move North", hotkey='n')

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name ="Move South", hotkey='s')

class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name="Move East", hotkey='e')

class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name="Move West", hotkey='w')


# Print out the players inventory
class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name="View Inventory", hotkey='i')

# Allow the player to attack
class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

# Applies an enchantment to a weapon
class Enchant(Action):
    def __init__(self):
        super().__init__(method=Player.enchant, name="Enchant", hotkey='p')
        
# Allow the Player to flee a battle
class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)
