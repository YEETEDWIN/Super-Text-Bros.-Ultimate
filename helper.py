#/bin/python3
import random, time 
from player import Player
###########################
#### Helper functions #####
###########################

# get_status() function: displays status of Player objects (user and bot) 
def get_status(user, bot): 
  print("-" * 40)
  bot.status() 
  user.status()
  print("-" * 40)

# user_move() function: asks user to choose a move, then does move against bot
# user and bot are both Player objects

def user_move(user, bot): 
  print("Choose a move:")
  
  for m in user.moves:                  # for each key in user.moves dictionary
    print(m)                            # print key (name of move)
  answer = input(">")
  answer = answer.lower()     
  while answer not in user.moves:       # repeats until user inputs valid move name
    print("Invalid")          
    answer = input(">")
    answer = answer.lower()         
  
  print(user.name, ":",  answer)
  move = user.moves[answer]             # looks up move in dictionary with key (name string)
  move(bot)                             # call user move against bot 
  
  time.sleep(1)                         # pause program for 1 second
  get_status(user, bot)

# bot_move() function: makes bot randomly do one of its moves against user 
# user and bot are both Player objects 

def bot_move(user, bot): 
  print("Computer's turn...")
  time.sleep(1)
  move_name = random.choice(list(bot.moves.keys()))   # randomly choose move name from dictionary
  move = bot.moves[move_name]                   # look up move in dictionary with key (name string)
  print(bot.name, ":", move_name)
  move(user)                   # call bot move against user
  time.sleep(1)
  get_status(user, bot)
  
  