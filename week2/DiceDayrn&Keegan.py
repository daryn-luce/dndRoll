import random

def addDie(Dice):
    return Dice[0] + Dice[1]

def Rolls():
    return [random.randint(1,6), random.randint(1,6)]

myList = []
dieList = []
for i in range(4):
    r = Rolls()
    dieList.append(addDie(r))
    myList.append(r)
    print(i)

dieList.sort()
print(dieList[:-1])
print (dieList)

for i, v in enumerate(dieList):
    print(v)
