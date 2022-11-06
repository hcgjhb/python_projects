import os
from art import logo

print(logo)
def add_bidders(name, bid):
  auction_bid[name]=bid

def highest_bid(dict):
  name=""
  maximum=0
  for key in dict:
    if(maximum < dict[key]):
      name = key
      maximum=dict[key]
  
  print(f"{name} is the one with highest bid of {dict[name]}")
  
auction_bid={}
while True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  add_bidders(name, bid)
  ques = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if ques=="yes":
    os.system('cls')
  elif ques=="no":
    os.system('cls')
    highest = highest_bid(auction_bid)
    print(highest)
    break