import random

possiblechoices = ["rock", "paper", "scissors"]

def RockPaperScissors():
   print("Welcome to Rock-Paper-Scissors")
   userchoice = input("Please enter your choice:")
   compchoice = random.choice(possiblechoices)
   print("The computer has chosen... " + str(compchoice))
   if (userchoice == "rock"):
      if (compchoice == "paper"):
         print("You have lost!")
      elif (compchoice == "scissors"):
         print("You have won!")
      elif (compchoice == "rock"):
         print("It's a tie!")
   elif (userchoice == "paper"):
      if (compchoice == "paper"):
         print("It's a tie!")
      elif (compchoice == "rock"):
         print("You have won!")
      elif (compchoice == "scissors"):
         print("You have lost!")
   elif (userchoice == "scissors"):
      if (compchoice == "rock"):
         print("You have lost!")
      elif (compchoice == "paper"):
         print("You have won!")
      elif (compchoice == "scissors"):
         print("It's a tie!")
   else:
      print("Invalid input.")

RockPaperScissors()