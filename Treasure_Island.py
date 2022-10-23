print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
dir = input("You are at a cross road. Where do you want to go? left or right\n")
dir = dir.lower()
if(dir == "left"):
    wait_or_swim = input("You come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swimlef to swim across\n ")
    wait_or_swim = wait_or_swim.lower()
    if(wait_or_swim == "wait"):
        door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        door = door.lower()
        if(door == "yellow"):
            print("You Win!")
        elif door == "red":
            print("Burned by fire. Game Over")
        elif door == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over")