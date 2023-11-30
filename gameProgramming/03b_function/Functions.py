import random
# FUNCTION  -- a named piece of code that can be reused easily.                                                                                                                                                                                                                                                                                                                                       HI! You Found me. 0w0
# FUNCTION SIGNATURE -- Syntax for creating a new function.
def exampleFunction(): # NO PARAMETERS
    count = 0
    num = int(input("How many times do you want to wish a happy birthday?\n"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1

def exampleFunctionB(num): # PARAMETERS
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION!
# exampleFunctionA()
# exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
    return sum # return will IMMEDIATELY exit a loop, function, if/elif/else block

rollDice(3, 6)
rollDice(1, 20)

strengthPlayer = rollDice(3, 6)
dexterityPlayer = rollDice(3, 6)
wisdomPlayer = rollDice(3, 6)

print(strengthPlayer)
print(dexterityPlayer)
print(wisdomPlayer)

def genStats():
    playerStats = [
        0, # STREGTH
        0, # DEXTERITY
        0, # CONSTITUTION
        0, # INTELLIGENCE
        0, # WISDOM
        0  # CHARISMA
    ]
    i = 0
    while i < 6:
        playerStats[i] = rollDice(3, 6) # STRENGTH
        i += 1
    playerStats[1] = rollDice(3, 6) # DEXTERITY
    playerStats[2] = rollDice(3, 6) # CONSITUTION
    playerStats[3] = rollDice(3, 6) # INTELLIGENCE
    playerStats[4] = rollDice(3, 6) #  WISDOM
    playerStats[5] = rollDice(3, 6) # CHARISMA

    print(playerStats)

genStats()















#CODE REVIEW BY CHICKENBUCKET