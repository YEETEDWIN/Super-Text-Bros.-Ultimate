#/bin/python3
import random, time
from player import Player


# Spiderman class
class Spiderman(Player): # create child class of Player
  def __init__(self):
    Player.__init__(self, "Spiderman") # use __init__ method from Player
    self.moves.pop("attack")
    self.moves["face punch"] = self.attack
    self.moves["web shooter"] = self.web_shooter # add new move to dictionary
    self.moves["flying kick"] = self.flying_kick
    self.moves["think"] = self.think

  def web_shooter(self, enemy): # new special move for child class
    self.attack(enemy, random.randint(40, 50))
  
  def flying_kick(self, enemy):
    if random.random() <= 0.75:
      damage = random.randint(35, 40)
      self.attack(enemy, damage)
    else:
      print("Spiderman didn't do a good kick...")
      time.sleep(1)
      damage = random.randint(20, 25)
      self.attack(enemy, damage)
  
  def think(self, enemy):
    self.energy += 0.15
    print(self.name + " has increased energy.")
    if self.energy >= 2: # if energy gets too high...
      self.moves.pop("think") # remove from dictionary of possible moves


# Pikachu class
class Pikachu(Player):
  def __init__(self):
    Player.__init__(self, "Pikachu")
    self.moves["thunder shock"] = self.thunder_shock
    self.moves["tail slap"] = self.tail_slap
    self.moves["pika block"] = self.pika_block
    self.moves["evolve"] = self.evolve
    self.specialmove = 2

# special move:
  def thunder_shock(self, enemy):
    damage = random.randint(40, 50)
    self.attack(enemy, damage)
    if random.random() <= 0.5: # 50% chance of lowering own health
      self.attack(self, 10)
  
  def tail_slap(self, enemy):
    self.attack(enemy, 35)
  
  def pika_block(self, enemy): # blocks 25 of enemy's attack
    print("Pikachu will get 20 health to block some of the enemy's attack.")
    self.health += 20
    time.sleep(1)
    self.attack(enemy, random.randint(30, 45))
  
  def evolve(self, enemy):
    self.name = "Raichu"
    self.health = 100
    print("Pikachu evolving ...")
    time.sleep(1)
    print("Pikachu evolved to Raichu!")
    self.moves.pop("thunder shock")
    self.moves.pop("tail slap")
    self.moves.pop("pika block")
    self.moves.pop("evolve")
    self.moves["thunder punch"] = self.thunder_punch
    self.moves["wild charge"] = self.wild_charge
    self.moves["raichu block"] = self.raichu_block
    self.moves["unevolve"] = self.unevolve
    self.specialmove1 = 2
  
  def thunder_punch(self, enemy):
    self.attack(enemy, random.randint(45, 50))
  
  def wild_charge(self, enemy):
    self.attack(enemy, random.randint(40, 50))
  
  def raichu_block(self, enemy):
    print("Raichu will get 25 health to block some of the attacks.")
    self.health += 25
    time.sleep(1)
    self.attack(enemy, random.randint(30, 45))
  
  def unevolve(self, enemy):
    self.name = "Pikachu"
    self.health = 100
    print("Raichu unevolved to Pikachu.")
    self.moves.pop("thunder punch")
    self.moves.pop("wild charge")
    self.moves.pop("raichu block")
    self.moves.pop("unevolve")
    self.moves["thunder shock"] = self.thunder_shock
    self.moves["tail slap"] = self.tail_slap
    self.moves["pika block"] = self.pika_block
    self.moves["evolve"] = self.evolve


# Hercules class
class Hercules(Player):
  def __init__(self):
    Player.__init__(self, "Hercules")
    self.moves["arrow shots"] = self.arrow_shots
    self.moves["club strike"] = self.club_strike
    self.moves["equalize healths"] = self.equalize_healths

  def arrow_shots(self, enemy):
    if random.random() <= 0.75:
      self.attack(enemy, random.randint(40, 45))
    else:
      print("Hercules missed!")
  
  def club_strike(self, enemy):
    self.attack(enemy, 35)
  
  def equalize_healths(self, enemy):
    if self.health < enemy.health:
      print("This move will make Hercules's health equal to the enemy's.")
      difference = enemy.health - self.health
      self.health += difference


# Jedi class
class Jedi(Player):
  def __init__(self):
    Player.__init__(self, "Jedi")
    self.moves.pop("attack") # remove old attack name
    self.moves["lightsaber slash"] = self.attack # rename basic attack move
    self.moves["force whirlwind"] = self.force_attack
    self.moves["battlemind"] = self.force_mind
    self.specialmove = 2 # track use of special move

# special support move (can only be used if energy is not too high)
  def force_mind(self, enemy):
    self.energy += 0.2 # increase energy (attack/heal strength)
    print("Meditation increases the concentration and willpower of " + self.name)
    print(self.name + " has increased energy.")
    if self.energy >= 1.8: # if energy gets too high...
      self.moves.pop("battlemind") # remove from dictionary of possible moves
  
  # special attack move (limited to 2 uses)
  def force_attack(self, enemy):
    self.attack(enemy, 60)
    self.specialmove -= 1 # subtract 1 use of specialmove
    if self.specialmove > 0:
      print(str(self.specialmove) + " time left to use this move.")
    else: # if 0 specialmove left
      time.sleep(1)
      print("You cannot use this move anymore.")
      self.moves.pop("force whirlwind") # remove from dict of possible moves
      

# Voldemort class
class Voldemort(Player):
  def __init__(self):
    Player.__init__(self, "Voldemort")
    self.moves.pop("attack")
    self.moves["crucio"] = self.attack
    self.moves["killing curse"] = self.avadakedavra
    self.moves["regeneration"] = self.heal
    self.moves["create horcrux"] = self.create_Horcrux

  def avadakedavra(self, enemy):
    print("AVADA KEDAVRA!")
    time.sleep(1) # wait 1 second
    if random.random() <= 0.75: # 3/4 chance attack will succeed
      self.attack(enemy, 50)
    else: # 1/4 chance that it will rebound
      print("Voldemort's curse rebounded!")
      self.attack(self, 50) # attacks himself!
  
  def create_Horcrux(self, enemy):
    if self.health <= 50:
      difference = 100 - self.health
      self.health += difference
      print("Voldemort got {} more health.".format(difference))
    else:
      self.health += 50
      print("Voldemort got 50 more health.")


# Thanos class
class Thanos(Player):
  def __init__(self):
    Player.__init__(self, "Thanos")
    self.moves["smash"] = self.smash
    self.moves["Thanos Snap"] = self.finger_snap


  def finger_snap(self, enemy):
    damage = random.randint(50, 70)
    self.attack(enemy, damage)

  def smash(self, enemy):
    damage = random.randint(25, 35)
    self.attack(enemy, damage)
    if random.random() < 0.5:
      self.attack(self, random.randint(5, 15))


# Medusa class
class Medusa(Player):
  def __init__(self):
    Player.__init__(self, "Medusa")
    self.moves.pop("attack")
    self.moves["claw slice"] = self.attack
    self.moves["stone attack"] = self.stone_attack
    self.moves["snake bite"] = self.snake_bite

  def stone_attack(self, enemy):
    print("DUCK!")
    time.sleep(1)
    if random.random() <= 0.5:
      self.attack(enemy, 50)
    else:
      print("The attack did nothing!")
  
  def claw_slice(self, enemy):
    self.attack(enemy, 35)
  
  def snake_bite(self, enemy):
    if random.random() <= 0.6:
      self.attack(enemy, random.randint(40, 45))
    else:
      time.sleep(1)
      print("The bite wasn't that bad!")
      self.attack(enemy, random.randint(15, 25))




