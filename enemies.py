#define a class for a generic enemy
class Enemy:

    # Constructor
    # Name - The name of the enemy
    # Health - How much HP the enemy currently has
    # Damage - How much damage the enemy can do
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    # Determines if the enemy is alive
    def is_alive(self):
        return self.health > 0


# Create a few examples of enemies
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         health=10,
                         damage=2)
        # Remember, is_alive is inherited by the enemy class

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",
                         health=30,
                         damage=15)
        # Remember, is_alive is inherited by the enemy class
