#!/bin/python3
import random, time, os, sys
from player import *
from special import *
from characters import *
from helper import *

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("Welcome to the battle game.")
print("")
time.sleep(1)

while True:

  chars = ['Spiderman', 'Pikachu', 'Hercules', 'Jedi', 'Samus','Voldemort', 'Thanos', 'Medusa', 'Mr.Game & Watch', 'Pit', 'Sonic','Ganondorf','Olimar','Mario','Falco','Wolf']
  secchars = ['R.O.B.','Meta Knight']

  print("Do you want to choose your character or do you want it to be random? (Type 'c' for choose and 'r' for random.)")
  answer = input(">")
  print("")


    
  if answer != 'c' and answer != 'r':
    while True:
      print("Invalid input.")
      answer = input(">")
      print("")
      
      if answer == 'c' or answer == 'r':
        break

  if answer == 'c':
    print("Choose one of the following characters to fight against the enemy!")
    print("")
    
    time.sleep(1)
    for char in chars:
      print(char)
    player = input(">")
    print("")
      
    if player not in chars and player not in secchars:
      while True:
        print("Please enter one of the characters mentioned above.")
        player = input(">")
        print("")
        
        if player in chars or player in secchars:
          break

  elif answer == 'r':
    player = random.choice(chars)
    print("Your character is...")
    time.sleep(1)
    print(player + "!")
    print("")
    time.sleep(1)

  oppose = random.choice(chars)

  if player == "Spiderman":
    user = Spiderman()
        
  elif player == "Pikachu":
    user = Pikachu()
      
  elif player == "Hercules":
    user = Hercules()
      
  elif player == "Jedi":
    user = Jedi()

  elif player == "Voldemort":
    user = Voldemort()

  elif player == "Thanos":
    user = Thanos()

  elif player == "Medusa":
    user = Medusa()

  elif player == "Samus":
    user = Samus()

  elif player == "Mr.Game & Watch":
    user = MrGameandWatch()

  elif player == "Pit":
    user = Pit()

  elif player == "Sonic":
    user = Sonic()

  elif player == "Ganondorf":
    user = Ganondorf()

  elif player == "R.O.B.":
    user = ROB()

  elif player == "Olimar":
    user = Olimar()

  elif player == "Mario":
    user = Mario()

  elif player == "Falco":
    user = Falco()

  elif player == "Wolf":
    user = Wolf()

  elif player == "Meta Knight":
    user = MetaKnight()

  if oppose == "Spiderman":
    bot = Spiderman()
        
  elif oppose == "Pikachu":
    bot = Pikachu()
      
  elif oppose == "Hercules":
    bot = Hercules()
      
  elif oppose == "Jedi":
    bot = Jedi()

  elif oppose == 'Voldemort':
    bot = Voldemort()

  elif oppose == 'Thanos':
    bot = Thanos()
    
  elif oppose == "Medusa":
    bot = Medusa()

  elif oppose == "Samus":
    bot = Samus()

  elif oppose == "Mr.Game & Watch":
    bot = MrGameandWatch()

  elif oppose == "Pit":
    bot = Pit()
  
  elif oppose == "Sonic":
    bot = Sonic()

  elif oppose == "Ganondorf":
    bot = Ganondorf()

  elif oppose == "R.O.B.":
    bot = ROB()

  elif oppose == "Olimar":
    bot = Olimar()

  elif oppose == "Mario":
    bot = Mario()

  elif oppose == "Falco":
    bot = Falco()

  elif oppose == "Wolf":
    bot = Wolf()

  elif oppose == "Meta Knight":
    bot = MetaKnight()

  print("The opponent that {} will be fighting against is...".format(player))
  time.sleep(1)
  print("{}!".format(oppose))
  time.sleep(3)
  clear()

  time.sleep(1)
  get_status(user, bot)
  if player == "Goku":
    sys.stdout.write("\033[F") #back to previous line 
    sys.stdout.write("\033[K") #clear line
    user.Kibar()
    print("-" * 40)
  time.sleep(1)

  while True:
    user_move(user, bot)
    if player == "Goku":
      sys.stdout.write("\033[F") #back to previous line 
      sys.stdout.write("\033[K") #clear line
      user.Kibar()
      print("-" * 40)
    time.sleep(1)
    
    if user.health <= 0:
      clear()
      print("{} has no more health...".format(player))
      time.sleep(1)
      print("Computer wins!")
      break

    elif bot.health <= 0:
      clear()
      print("{} has no more health...".format(oppose))
      time.sleep(1)
      print("You win!")
      break
    
    bot_move(user, bot)
    if player == "Goku":
      sys.stdout.write("\033[F") #back to previous line 
      sys.stdout.write("\033[K") #clear 
      user.Kibar()
      print("-" * 40)
    time.sleep(1)
    
    if user.health <= 0:
      clear()
      print("{} has no more health...".format(player))
      time.sleep(1)
      print("Computer wins!")
      break

    elif bot.health <= 0:
      clear()
      print("{} has no more health...".format(oppose))
      time.sleep(1)
      print("You win!")
      break
  
  time.sleep(1)
  print("__________________________________________")
  time.sleep(1)
  print("Want to play another round? y/n")
  time.sleep(1)
  new_round = input(">")

  while new_round != 'y' and new_round != 'yes' and new_round != 'n' and new_round != 'no':
    print("")
    print("Invalid input.")
    clear()
    time.sleep(1)
    new_round = input(">")
  
  if new_round == 'y' or new_round == 'yes':
    clear()
    print("")
  
  elif new_round == 'n' or new_round == 'no':
    clear()
    print("")
    print("Okay then.")
    break
  
      
      
    