import random

#List of Options
options = ['rock', 'paper', 'scissors']

# Get Choice from User
user_choice = input("Choose rock, paper, or scissors:")

#validate input
if user_choice not in options:
    print ("Invalid Choice Please try again")
    exit()

#have the computer make a random choice
computer_choice = random.choice(options)
#print (computer_choice)
#compare choices to pick the winner

if user_choice == computer_choice:
    print ("It's a tie")
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
    print ("You Win!")
else:
    print ("You Loose")