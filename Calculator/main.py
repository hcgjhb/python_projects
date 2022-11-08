from art import logo
import os
def add(a, b):
  return a+b

def subtract(a, b):
  return a-b

def multiply(a, b):
  return a*b

def divide(a, b):
  return a/b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
def calculator():
  print(logo)
  num1 = float(input("Enter the first number: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation ")
    num2 = float(input("Enter the next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation.\n")=='y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls')
      calculator()
    
calculator()