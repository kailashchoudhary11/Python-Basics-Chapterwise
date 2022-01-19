import random

def game(p, c):
    if (p == "g" and c == "w"):
       print("Computer is winner!")
       return
    elif (p == "g" and c == "s"):
       print("You are winner!")
       return
    elif (p == "w" and c == "g"):
       print("You are winner!")
       return
    elif (p == "w" and c == "s"):
       print("Computer is winner!")
       return
    elif (p == "s" and c == "g"):
       print("Computer is winner!")
       return
    elif (p == "s" and c == "w"):
       print("You are winner!")
       return
    else:
        print("Draw")
    

randNo = random.randint(1, 3)
if (randNo == 1):
    comp = "s"
elif(randNo == 2):
    comp = "w"
else:
    comp = "g"

you = input("Your Turn: Press s(snake), w(water), g(gun): ")
print("Computer's choice is " + comp)
game(you, comp)
