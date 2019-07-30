import random

# Rolls random number 1-6 
def die():
    return random.randint(1,6)

# Rolls set of die how ever the amount returns list
def roll(amount):
    rollList = []
    for i in range(amount):
        rollList.append([die(),die()])
    return rollList

# Sorts list and returns first 3    
def bestOf(diceList,qty):
    diceList.sort(reverse=True)
    return(diceList[:qty])
    
# Returns the sum of the List
def diceSum(diceList):
        return sum(diceList)
        
dice = []
print('Rolls')
for die1,die2 in roll(4):
    dice.append(die1 + die2)
    print('{} and {} : {}'.format(die1,die2,(die1 + die2)))

diceList = bestOf(dice,3)

print('-----')
print('Best')
for die in diceList:
    print(die)

print('------')
print('Sum of Best')
print(diceSum(diceList))

    