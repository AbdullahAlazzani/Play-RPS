"""
Abdullah Alazzani
Plays a Game of Rock, Paper, and scissors
"""
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!",
  "error": "That's not a valid game. Check your spelling!"
}

def decide_winner(user_choice, computer_choice):  # function implementation
  print ("You selected %s" % user_choice) 
  print ("Computer selected %s" % computer_choice)
  if user_choice == computer_choice:
    print (message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
      print (message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
      print (message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print (message["won"])
  elif user_choice == options[0] and computer_choice == options[1]:
      print (message["lost"])
  elif user_choice == options[1] and computer_choice == options[2]:
      print (message["lost"])
  elif user_choice == options[2] and computer_choice == options[0]:
    print (message["lost"])
  else:
    print (message["error"])
      
def play_RPS():
  while True:
    user_choice = input("Enter Rock, Paper, or Scissor: ").upper()

    if user_choice == "STOP":
      break
    
    computer_choice = options[randint(0,2)]
    decide_winner(user_choice, computer_choice) # function call
    print (" Print Stop if you want to Stop the Game!")
play_RPS()
