import random
from art import logo
print(logo)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
attempts=0
if level == 'easy':
  attempts = 10
else:
  attempts = 5
num=random.randint(1, 100)
check = 0
while attempts!=0:
  print(f"You have {attempts} remaining to guess a number")
  guess_num = int(input("Make a guess: "))
  if guess_num==num:
    print(f"You got it. The answer was {num}")
    check=1
    break
  elif guess_num>num:
    print("Too high")
    
  else:
    print("Too low")
  attempts-=1
   

if(check==0):
  print("You have run out of guesses. You lose")