from random import randint



def rollDie(d,sd):
    dice =[]
    for l in range(d):
        dice.append(randint(0,sd))
    return dice


dieRolls = ["5d12","6d4","1d2","1d8","3d6","4d20","100d100"]

for die in dieRolls:
    d,n = map(int,die.split("d"))
    krolls = rollDie(d,n)
    print(sum(krolls), krolls)

        