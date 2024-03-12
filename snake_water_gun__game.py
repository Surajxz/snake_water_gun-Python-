import random
def game_win(comp,you):
    if comp == you:
        return  None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False 
        

rand_no=random.randint(1,3)
if rand_no == 1:
    comp = "s"
elif rand_no == 2:
    comp = "w"
elif rand_no == 3:
    comp = "g"

#comp=input("comp.turn: choose snake-s or water-w or gun-g")
you=input("your turn: choose snake-s or water or gun-g  =    ")
a = game_win(comp,you)
print("computer coose ------>",comp)
print("you choose------------>",you)
if a == None:
    print("match tie !!!")
elif a:
    print("you win  .............yeahh !!!")
else:
    print("you lose the game !!!!!!!!!!")
"""import  random
a=(random.randint(1,2))
print(a)"""