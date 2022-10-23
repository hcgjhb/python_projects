print("Welcome to Python Pizza Deliveries")
size = input("What pizza do you want? S, M or L? ")
add_pepporoni = input("Do you want pepporoni? ")
extra_cheese = input("Do you want extra chesse? ")

if(size == "S"):
    if(add_pepporoni == "Y"):
        if(extra_cheese == "Y"):
            bill = 15+2+1
            print("Your final bill is: $",bill)
        else:
            bill = 15+2
            print("Your final bill is: $",bill)
    else:
        if(extra_cheese == "Y"):
            bill = 15+1
            print("Your final bill is: $",bill)
        else:
            bill = 15
            print("Your final bill is: $",bill)
elif(size=="M"):
    if(add_pepporoni == "Y"):
        if(extra_cheese == "Y"):
            bill = 20+3+1
            print("Your final bill is: $",bill)
        else:
            bill = 20+3
            print("Your final bill is: $",bill)
    else:
        if(extra_cheese == "Y"):
            bill = 20+1
            print("Your final bill is: $",bill)
        else:
            bill = 20
            print("Your final bill is: $",bill)
elif(size=="L"):
    if(add_pepporoni == "Y"):
        if(extra_cheese == "Y"):
            bill = 25+3+1
            print("Your final bill is: $",bill)
        else:
            bill = 25+3
            print("Your final bill is: $",bill)
    else:
        if(extra_cheese == "Y"):
            bill = 25+1
            print("Your final bill is: $",bill)
        else:
            bill = 25
            print("Your final bill is: $",bill)