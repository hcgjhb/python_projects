import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
if(choice == 0 and computer_choice == 0):
  print(rock)
  print("Computer chose")
  print(rock)
  print("It's a draw")
elif(choice == 0 and computer_choice == 1):
  print(rock)
  print("Computer chose")
  print(paper)
  print("You lose")
elif(choice == 0 and computer_choice == 2):
  print(rock)
  print("Computer chose")
  print(scissors)
  print("You win")
elif(choice == 1 and computer_choice == 0):
  print(paper)
  print("Computer chose")
  print(rock)
  print("You win")
elif(choice == 1 and computer_choice == 1):
  print(paper)
  print("Computer chose")
  print(paper)
  print("It's a draw")
elif(choice == 1 and computer_choice == 2):
    print(paper)
    print("Computer chose")
    print(scissors)
    print("You lose")
elif(choice == 2 and computer_choice == 0):
    print(scissors)
    print("Computer chose")
    print(rock)
    print("You lose")
elif(choice == 2 and computer_choice == 1):
    print(scissors)
    print("Computer chose")
    print(paper)
    print("You win")
elif(choice == 2 and computer_choice == 2):
    print(scissors)
    print("Computer chose")
    print(scissors)
    print("It's a draw")