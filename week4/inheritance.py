class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        print(f"{self.name} has attacked")
        
class Player(Character):
    def __init__(self, name, health, level):
        super().__init__(name, health)
        self.level = level
        
    def heal(self, amount):
        self.health += amount
        print(f"{self.name}'s Current Health: {self.health}")
    
    def attack(self):
        print(f"{self.name} has fired a laser beam")
        

class Enemy(Character):

    def __init__(self, name, health, enemy_type):
        super().__init__(name, health)
        self.enemy_type = enemy_type

    def defend(self):
        print(f"{self.name} has used their shield")

    def attack(self):
        print(f"{self.name} has fired a missile")


player = Player("pacman", 10, 100000000000)
Enemy =  Enemy("Gob", 100000000000000000000000000000000000000000000000000000000, "Goblin")

player.attack()
Enemy.attack()
player.attack()
Enemy.attack()

player.heal(10)
Enemy.defend()
print(Enemy.health)