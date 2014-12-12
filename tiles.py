import items, questItems, enemies, actions, world, random

# abstract
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define a method for when the player enters the tile
    def intro_text(self):
        raise NotImplementedError()

    # define a method for what happens to the player
    def modify_player(self, player):
        raise NotImplementedError()

    # return a list of available movements based on the adjacent tiles
    def adjacent_moves(self):

        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())

        return moves

    # return a list of all available actions for the room
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Enchant())

        return moves


# Lets create some tile subclasses

# The start room with the introduction to the game
class StartingRoom(MapTile):

    
    def intro_text(self):
        return """
        This is my first shot at making a text based adventure game. I hope it comes
        out nice. You start in a spooky cave as usual and there are four paths to take
        """

    def modify_player(self, player):
        #This is the start room so nothing happens to the player
        pass

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        Congratulations! You've made it out of the cave!
        """

    def modify_player(self, player):
        player.victory = True

# Randomly generates a room based off some random number
class RandomEventRoom(MapTile):
    random = random.randint(1,2)

    def intro_text(self):
        if random == 0: # Generate empty room
            return EmptyPath.intro_text()
        if random == 1:
            return GiantSpiderRoom.intro_text()
        if random == 2:
            return DaggerRoom.intro_text()

    def modify_player(self, player):
        if random == 0:
            return EmptyPath.modify_player(player)
        if random == 1:
            return GiantSpiderRoom.modify_player(player)
        if random == 2:
            return DaggerRoom.modify_player(player)
    
# A room where the player finds a new item (Abstract)
class LootRoom(MapTile):
    
    #Constructor
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    # adds loot to the players inventory
    def add_loot(self, player):
        player.inventory.append(self.item)
    
    # modify the player of course
    def modify_player(self, player):
        self.add_loot(player)


# A room where the player encounters an enemy
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        # if the enemy is alive, do battle with it
        if self.enemy.is_alive():
            player.health = player.health - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.health))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

# An empty room with nothing interesting
class EmptyPath(MapTile):

    def intro_text(self):
        return """
        There's nothing interesting here, you decide to move forward.
        """

    def modify_player(self, player):
        pass


# An Enemy room containing a spider
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Zoinks Scoob! That's a big spider, and he doesn't look friendly!
            """
        else:
            return """
            While the spider may be dead, I still have any Scooby Snacks.
            """

# An Enemy room containing an ogre
class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Zoinks Scoob! That's a big Ogre, and he doesn't look friendly!
            """
        else:
            return """
            While the Ogre may be dead, I still don't have any Scooby Snacks.
            """


# A room containing a new dagger for the hero
class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You find yourself a brand spankin\' new Dagger!
        """

# A room containing a new rock for the hero
class FindRockRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Rock())

    def intro_text(self):
        return """
        You find yourself a brand spankin\' new Rock! Hardcore!
        """

# A room containing a new Fire Stone for the hero
class FireStoneRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.FireStone())
        
    def intro_text(self):
        return """
        You find yourself a brand spankin\' new FireStone! Smokin!
        """


# A room containing gold!
class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(100))

    def intro_text(self):
        return """
        Lovely, Money! You found: {}\n""".format(self.item)
                  













                
