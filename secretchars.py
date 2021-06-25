import random, time, sys
from player import Player
from operator import add, mul, sub, truediv
from getkey import getkey, keys

class MetaKnight(Player):

  def __init__(self):
    Player.__init__(self, "Meta Knight")
    self.moves.pop("attack")
    self.moves["mach tornado"] = self.attack
    self.moves["drill rush"] = self.drill_rush
    self.moves.pop("heal")
    self.moves["shuttle loop"] = self.shuttle_loop
    self.moves["dimensional cape"] = self.cape
    self.moves["galaxia darkness"] = self.darkness
    self.movescount = 2

  def drill_rush(self, enemy):
    choices = ['UP','DOWN','RIGHT','LEFT']
    print("Press up, down, right or left!")
    direction = random.choice(choices)
    key = getkey()
    if key == keys.UP:
      if direction == 'UP':
        damage = random.randint(35,55)
        print('Correct choice, extra damage')
        time.sleep(1)
      else:
        damage = random.randint(15,25)
        print('Incorrect choice, decrease damage')
        time.sleep(1)
    elif key == keys.DOWN:
      if direction == 'DOWN':
        damage = random.randint(35,55)
        print('Correct choice, extra damage')
        time.sleep(1)
      else:
        damage = random.randint(15,25)
        print('Incorrect choice, decrease damage')
        time.sleep(1)
    elif key == keys.RIGHT:
      if direction == 'RIGHT':
        damage = random.randint(35,55)
        print('Correct choice, extra damage')
        time.sleep(1)
      else:
        damage = random.randint(15,25)
        print('Incorrect choice, decrease damage')
        time.sleep(1)
    elif key == keys.LEFT:
      if direction == 'LEFT':
        damage = random.randint(35,55)
        print('Correct choice, extra damage')
        time.sleep(1)
      else:
        damage = random.randint(15,25)
        print('Incorrect choice, decrease damage')
        time.sleep(1)
    else:
      print('You wasted your turn by clicking something else')
    self.attack(enemy, damage)

  def shuttle_loop(self, enemy):
    if random.random() <= 0.5:
      self.attack(enemy, 20)
    self.heal(self)

  def cape(self, enemy):
    self.energy += 0.2
    print("I shall hide myself and increase my power")
    print(self.name + " has increased energy.")
    if self.energy >= 2:
      self.moves.pop("dimensional cape")
  
  def darkness(self, enemy):
    self.attack(enemy, 60)
    self.movescount -= 1 # subtract 1 use of specialmove
    if self.movescount > 0:
      print(str(self.movescount) + " time left to use this move.")
    else: # if 0 specialmove left
      time.sleep(1)
      print("You cannot use this move anymore.")
      self.moves.pop("galaxia darkness") # remove from dict of possible moves