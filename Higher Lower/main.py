import random
import art
from game_data import data
import os


def check(A, B):
  ans = input("Who has more followers? Type 'A' or 'B': ")
  if(A[0]['follower_count'] > B[0]['follower_count'] and ans=='A'):
    return True
  elif(A[0]['follower_count'] < B[0]['follower_count'] and ans=='A'):
    return False
  elif(A[0]['follower_count'] > B[0]['follower_count'] and ans=='B'):
    return False
  elif(A[0]['follower_count'] < B[0]['follower_count'] and ans=='B'):
    return True

is_answer_correct = True
count=0
A=[]
i=0
A.append(random.choice(data))
while is_answer_correct:
  print(art.logo)
  
  print(f"Current Score: {count}")
  print(f"Compare A: {A[i]['name']}, {A[i]['description']}, from {A[i]['country']}")
  
  print(art.vs)
  
  B=[]
  B.append(random.choice(data))
  while B[0] in A:
    B.clear()
    B.append(random.choice(data))
  print(f"Against B: {B[0]['name']}, {B[0]['description']}, from {B[0]['country']}")
  if check(A, B) == True:
    count+=1
    os.system('cls')
    A.append(B[0])
    B.clear()
    i+=1
  else:
    is_answer_correct = False
    os.system('cls')

print(art.logo)
print(f"Sorry. That's wrong. Final score is {count}")