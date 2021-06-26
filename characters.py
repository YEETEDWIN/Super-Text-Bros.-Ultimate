#/bin/python3
import random, time
from player import Player
from getkey import getkey, keys
from threading import Thread

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
    self.moves["pikmin throw"] = self.throw
    self.moves["end of day"] = self.endofday
    self.pikmins = 5
    self.poison = 5

    self.redpikmin = 1
    self.whitepikmin = 1
    self.yellowpikmin = 1
    self.purplepikmin = 1
    self.bluepikmin = 1

  def pluck(self, enemy):
    def redpikmin():
      damage = 30
      self.attack(enemy, damage)
    
    def yellowpikmin():
      damage = 17
      if random.random() >= 0.6:
        damage*2
      self.attack(enemy, damage)

    def whitepikmin():
      damage = 10
      damage += self.poison
      self.poison += 5
      self.attack(enemy, damage)
    
    def purplepikmin():
      damage = 35
      self.attack(enemy, damage)
    
    def bluepikmin():
      damage = random.randint(15,25)
      self.attack(enemy, damage)

    self.pikmins += 1
    pikminchoices = [redpikmin, yellowpikmin, whitepikmin, purplepikmin, bluepikmin]
    choice = random.choice(pikminchoices)
    if choice == redpikmin:
      self.redpikmin += 1
      self.pikmins += 1
    elif choice == yellowpikmin:
      self.yellowpikmin += 1
      self.pikmins += 1
    elif choice == purplepikmin:
      self.purplepikmin += 1
      self.pikmins += 1
    elif choice == whitepikmin:
      self.whitepikmin += 1
      self.pikmins += 1
    elif choice == bluepikmin:
      self.bluepikmin += 1
      self.pikmins += 1
    choice()
  
  def throw(self, enemy):
    def redpikmin():
      damage = 30
      self.attack(enemy, damage)
    
    def yellowpikmin():
      damage = 17
      if random.random() >= 0.6:
        damage*2
      self.attack(enemy, damage)

    def whitepikmin():
      damage = 10
      damage += self.poison
      self.poison += 5
      self.attack(enemy, damage)
    
    def purplepikmin():
      damage = 35
      self.attack(enemy, damage)
    
    def bluepikmin():
      damage = random.randint(15,25)
      self.attack(enemy, damage)
    
    pikminchoices = ['red', 'yellow', 'white', 'purple', 'blue']
    choice = random.choice(pikminchoices)
    if choice == 'red':
      for pikmin in range(self.redpikmin):
        redpikmin()
        time.sleep(0.2)
    elif choice == 'yellow':
      for pikmin in range(self.yellowpikmin):
        yellowpikmin()
        time.sleep(0.2)
    elif choice == 'purple':
      for pikmin in range(self.purplepikmin):
        purplepikmin()
        time.sleep(0.2)
    elif choice == 'white':
      for pikmin in range(self.whitepikmin):
        whitepikmin()
        time.sleep(0.2)
    elif choice == 'blue':
      for pikmin in range(self.bluepikmin):
        bluepikmin()
        time.sleep(0.2)

  def endofday(self, enemy):
    damage = self.pikmins*7
    self.attack(enemy, damage)


# Mario class
class Mario(Player):
  def __init__(self):
    Player.__init__(self, "Mario")
    self.moves.pop("attack")
    self.moves["fireball"] = self.attack
    self.moves["super jump punch"] = self.punch
    self.moves["f.l.u.d.d."] = self.fludd
    self.moves["mario finale"] = self.mario
    self.waterpwr = 1

  def punch(self, enemy):
    self.attack(enemy, 30)
  
  def fludd(self, enemy):
    damage = 20*self.waterpwr
    self.attack(enemy, damage)
    self.waterpwr+=0.4
  
  def mario(self, enemy):
    self.energy+=0.2
    self.attack(enemy, 30)

# Falco class
class Falco(Player):
  def __init__(self):
    Player.__init__(self, "Falco")
    self.moves.pop("attack")
    self.moves["blaster"] = self.attack
    self.moves["falco phantasm"] = self.phantasm
    self.moves["reflector"] = self.reflector
    self.moves["land master"] = self.landmaster

  def phantasm(self, enemy):
    if random.random() <= 0.1:
      print("SLICE")
      self.attack(enemy, 60)
    else:
      self.attack(enemy, 20)
  
  def reflector(self, enemy):
    if random.random() <= 0.2:
      print("REFLECTIONNNNNN-!")
      damage = enemy.health/2
      round(damage)
      self.attack(enemy, damage)
    else:
      damage = enemy.health/4
      round(damage)
      self.attack(enemy, damage)
    
  def landmaster(self, enemy):
    answer1 = None
    choices = ["ABOVE","DOWN","LEFT","RIGHT"]
    direction1 = random.choice(choices)

    def check1():
      time.sleep(2)
      if answer1 != None:
        if answer1 == direction1:
          self.attack(enemy, 50)
          return
        else:
          print("Not correct choice you lose a turn \npress enter to continue")
          return
      print("Too slow, you lose a turn\npress enter to continue")

    if direction1 == "ABOVE":
      Thread(target = check1).start()
      answer1 = input("Type in ABOVE\n>")
    elif direction1 == "DOWN":
      Thread(target = check1).start()
      answer1 = input("Type in DOWN\n")
    elif direction1 == "LEFT":
      Thread(target = check1).start()
      answer1 = input("Type in LEFT\n")
    elif direction1 == "RIGHT":
      Thread(target = check1).start()
      answer1 = input("Type in RIGHT\n")


