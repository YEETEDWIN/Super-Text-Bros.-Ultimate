#/bin/python3
import random, time
from player import Player
from getkey import getkey, keys


# R.O.B. class
class ROB(Player):
  def __init__(self):
    Player.__init__(self, "R.O.B.")
    self.moves.pop("attack")
    self.moves["robo beam"] = self.robo_beam
    self.moves["arm rotor"] = self.arm_rotor
    self.moves.pop("heal")
    self.moves["robo burner"] = self.robo_burner
    self.moves["speedy gyro"] = self.gyro
    self.speed = 10

  def robo_beam(self, enemy, damage=-1):
    if damage == -1:                   # if there is no 2nd argument 
      damage = random.randint(20, 40)     # random number for damage
    damage *= self.energy              # multiplies damage by energy level
    damage = round(damage)
    enemy.health -= damage
    print(self.name, "did", damage, "damage to", enemy.name)
    self.speed += 10
    if self.speed >= 80:
      self.moves["diffusion beam"] = self.diffuse_beam
      print('You earned enough speed to use "diffusion beam"')

  def arm_rotor(self, enemy):
    damage = self.speed
    print("I have grinded all my speed into my core!")
    self.attack(enemy, damage)
    self.speed = 0
  
  def robo_burner(self, enemy):
    print("I shall fly and escape!")
    speed = self.speed
    n = random.randint(25, 40)
    speed -= n
    n *= self.energy
    self.health += round(n) 
    print(self.name, "healed self", n)
    self.attack(enemy, 10)
    self.speed += 10
    if self.speed >= 80:
      self.moves["diffusion beam"] = self.diffuse_beam
      print('You earned enough speed to use "diffusion beam"')

  def gyro(self, enemy):
    print("I shall earn more speed")
    gyro_speed = random.randint(1,30)
    luck = random.random()
    if gyro_speed > 23 and luck > 0.5:
      self.speed = 10
      print("You got too much speed so due this you didn't get any.\nNow you have 10 speed.")
    else:
      self.speed += gyro_speed
      print("You got more speed.\nNow you have "+str(self.speed)+" speed")
    if self.speed >= 80:
      self.moves["diffusion beam"] = self.diffuse_beam
      print('You earned enough speed to use "diffusion beam"')
    
  def diffuse_beam(self, enemy):
      self.attack(enemy, 100)
      self.speed = 0
      self.moves.pop("diffusion beam")


# Ganondorf class
class Ganondorf(Player):
  def __init__(self):
    Player.__init__(self, "Ganondorf")
    self.moves.pop("attack")
    self.moves["warlock punch"] = self.warlock_punch
    self.moves["flame choke"] = self.flame_choke
    self.flame = 0
    self.movescount = 0

  def warlock_punch(self, enemy, damage=-1):
    self.movescount += 1 
    if damage == -1:                   # if there is no 2nd argument 
      damage = random.randint(20, 40)     # random number for damage
    damage *= self.energy              # multiplies damage by energy level
    damage = round(damage)
    enemy.health -= damage
    print(self.name, "did", damage, "damage to", enemy.name)
    if self.movescount >= 3:
      self.moves["beast ganon"] = self.beast_ganon
      print('You earned the "beast ganon" ability')

  def flame_choke(self, enemy):
    self.movescount += 1
    damage = random.randint(20,30)
    if self.flame >= 1:
      damage = damage + 5
    if self.flame > 3:
      damage = damage + 20
    self.attack(enemy, damage)
    self.flame += 1
    if self.movescount >= 3:
      self.moves["beast ganon"] = self.beast_ganon
      print('You earned the "beast ganon" ability')

  def beast_ganon(self, enemy):
    self.flame = 0
    self.moves["dark dive"] = self.dark_dive
    self.moves.pop("flame choke")
    self.moves.pop("beast ganon")
    damage = random.randint(25,45)
    self.attack(enemy, damage)
  
  def dark_dive(self, enemy):
    damage = random.randint(30,45)
    if self.flame >= 1:
      damage = damage + 10
    if self.flame > 5:
      damage = damage + 40
    self.attack(enemy, damage)
    self.flame += 2


# Sonic class
class Sonic(Player):
  def __init__(self):
    Player.__init__(self, "Sonic")
    self.moves.pop("attack")
    self.moves["homing attack"] = self.homing_attack
    self.moves["spin dash"] = self.spin_dash
    self.movescount = 0

  def homing_attack(self, enemy, damage=-1):
    self.movescount += 1 
    if damage == -1:                   # if there is no 2nd argument 
      damage = random.randint(20, 40)     # random number for damage
    damage *= self.energy              # multiplies damage by energy level
    damage = round(damage)
    enemy.health -= damage
    print(self.name, "did", damage, "damage to", enemy.name)
    if self.movescount >= 3:
      self.moves["super sonic"] = self.super_sonic
      print("You just earned the 'super sonic' ability")

  def spin_dash(self, enemy):
    self.movescount += 1
    speed = random.randint(2,12)
    if speed == 7:
      damage = 40
    elif speed > 7:
      damage = 15
    elif speed < 7:
      damage = 25
    self.attack(enemy, damage)
    if self.movescount >= 3:
      self.moves["super sonic"] = self.super_sonic
      print("You just earned the 'super sonic' ability")

  def super_sonic(self, enemy):
    self.energy += 1.7 # increase energy (attack/heal strength)
    print("I am now super SONIC mode!")
    print(self.name + " has increased their energy.")
    self.moves.pop("super sonic") # remove from dictionary of possible moves
      

# Pit class
class Pit(Player):
  def __init__(self):
    Player.__init__(self, "Pit")
    self.moves.pop("attack")
    self.moves["palutena's arrow"] = self.attack
    self.moves["wings of icarus"] = self.wings_icarus
    self.moves["palutena's army"] = self.army

  def wings_icarus(self, enemy):
    print("I Pit, shall fly to heaven!")
    time.sleep(1)
    if random.random() <= 0.7:
      heal = random.randint(20,50)
      self.health += heal
      print("Pit healed himself of "+ str(heal) +" health.")
      self.attack(enemy, 20)
    else:
      print("No I fell!")
      self.attack(self, 20)
      self.attack(enemy, 20)
  
  def army(self, enemy):
    print("My army of minions shall devour you!")
    time.sleep(1)
    minions =  random.randint(3,15)
    damage = minions*6
    self.attack(enemy, damage)


# Mr.Game & Watch class
class MrGameandWatch(Player):
  def __init__(self):
    Player.__init__(self, "Mr. Game & Watch")
    self.moves.pop("attack")
    self.moves["judge"] = self.attack
    self.moves["oil panic"] = self.oil_panic
    self.moves["octopus"] = self.octopus

  def oil_panic(self, enemy):
    print("Get Burnt... Please")
    time.sleep(1)
    if random.random() <= 0.6:
      self.attack(enemy, 60)
    else:
      print("The oil failed to burn!")

  def octopus(self, enemy):
    print("Big 2D Mode!")
    time.sleep(1)
    damage = random.randint(30,50)
    self.attack(enemy, damage)


# Samus class
class Samus(Player):
  def __init__(self):
    Player.__init__(self, "Samus")
    self.moves.pop("attack")
    self.moves["charge shot"] = self.attack
    self.moves["missile shot"] = self.missile
    self.moves["zero laser"] = self.zero_laser

  def missile(self, enemy):
    print("EXPLODEE!")
    time.sleep(1)
    if random.random() <= 0.75:
      self.attack(enemy, random.randint(20,35))
    else:
      print("You shot next to yourself!")
      self.attack(self, random.randint(20,40))
    
  def zero_laser(self, enemy):
    print("Infinitive LASER!!!")
    time.sleep(1)
    if random.random() <= 0.2:
      damage = (enemy.health)*0.9
      self.attack(enemy, damage)
      self.attack(self, 20)
    else:
      print("Failed LASER!!!")
      self.attack(self, 20)


# Pikmin & Olimar class
class Olimar(Player):
  def __init__(self):
    Player.__init__(self, "Olimar")
    self.moves.pop("attack")
    self.moves["pikmin pluck"] = self.pluck
    self.moves["missile shot"] = self.missile
    self.moves["zero laser"] = self.zero_laser
    self.pikmins = []
    self.poison = 5

  def pluck(self, enemy):

    def redpikmin(self, enemy):
      damage = 30
      self.attack(enemy, damage)
    
    def yellowpikmin(self, enemy):
      damage = 17
      if random.random() >= 0.6:
        damage*2
      self.attack(enemy, damage)

    def whitepikmin(self, enemy):
      damage = 10
      damage += self.poison
      self.poison += 5
      self.attack(enemy, damage)
    
    def purplepikmin(self, enemy):
      damage = 35
      self.attack(enemy, damage)

    pikminchoices = [redpikmin, yellowpikmin, whitepikmin, purplepikmin]
    choice = random.choice(pikminchoices)
    choice()
