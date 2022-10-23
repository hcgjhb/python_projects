print("welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total = (tip/100) * bill + bill
a = total/people
print(a)