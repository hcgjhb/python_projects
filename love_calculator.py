

print("Welcome to the Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')
l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')
sum = (t+r+u+e)*10 + l+o+v+e
if sum < 10 or sum > 90:
    print(f'Your score is {sum}, you go together like coke and mentos')
elif sum > 40 and sum < 50:
    print(f'Your score is {sum}, you are alright together')
else:
    print(f'Your score is {sum}')