import random

# Rolls random number 1-6 
def die(sides):
    return random.randint(1,sides)

# Rolls set of die how ever the amount returns list
def roll(amount,sides1,sides2):
    rollList = []
    for i in range(amount):
        rollList.append([die(sides1),die(sides2)])
    return rollList

# Sorts list and returns first 3    
def bestOf(diceList,qty):
    diceList.sort(reverse=True)
    return(diceList[:qty])
    
# Returns the sum of the List
def diceSum(diceList):
        return sum(diceList)
        
amount_rolls = 4
amount_best = 3
die1_sides = 6
die2_sides = 6
dice = []

print('Rolls')
for die1,die2 in roll(amount_rolls,die1_sides,die2_sides):
    dice.append(die1 + die2)
    print('{} and {} : {}'.format(die1,die2,(die1 + die2)))

diceList = bestOf(dice,amount_best)

print('-----')
print('Best')
for die in diceList:
    print(die)

print('------')
print('Sum of Best')
print(diceSum(diceList))

    