#/bin/python3
import random, time

class Player:
  
  # __init__() method initializes new instance of Player
  def __init__(self, name): 
    self.name = name                          
    self.health = 100 
    self.energy = 1
    self.ki = 100
    self.moves = {}                           # create dictionary of moves
    
    # moves property is a dictionary - used to look up a Player's moves    
    # key = string (name of move), value = method (function for move)  
    
    self.moves["attack"] = self.attack        # add attack move to dictionary
    self.moves["heal"] = self.heal            # add heal move to dictionary
  
  
  # status() method prints out a Player's name and health properties    
  def status(self): 
    print(self.name, " health: ", self.health)
  
  def Kibar(self):
    print(self.name, " ki bar: ", self.ki)
    
  # attack() method: move that lowers health of enemy Player 
  # enemy: Player object 
  # damage: integer (optional). If no 2nd argument given, does random damage.
 
  def attack(self, enemy, damage=-1): 
    if damage == -1:                   # if there is no 2nd argument 
      damage = random.randint(20, 40)     # random number for damage
    damage *= self.energy              # multiplies damage by energy level
    damage = round(damage)
    enemy.health -= damage
    print(self.name, "did", damage, "damage to", enemy.name)
     
      
  # heal() method: move that increases a Player's own health (by random amount)  
  # enemy: Player object 
  
  def heal(self, enemy):
    n = random.randint(25, 45)        # random number for health increase 
    n *= self.energy                  # multiplied by energy level
    self.health += round(n) 
    print(self.name, "healed self", n)
  
  






