# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # Tell them guess is correct.
    # Award a point
# What happens if the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if the player or CPU has >= 3 points, if so they win.

# Guess a Number, Ryan Kelley, v0.0
import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1 
playerScore = 0 
cpuScore = 0
numGuesses = 0
playerName = ""
# You are missing some of the variables.  

print("""
        *~~~~~~~~~~~~~~~~~~~~~~~~*
        |                        |
        |    Guess a Number      |
        |     Trevis Brown       |
        |        2023            |
        |                        |
        |                        |
        *~~~~~~~~~~~~~~~~~~~~~~~~*

        """)
# CPU SECRET NUMBER GENERATION
x = 0
while x < 50:
    secretNumber = random.randint(0,20)
    print(secretNumber)
    x += 1
print("You need to guess a number from 0 to 20 and you have four guesses. \nIf you guess it right, you get a point. \nIf you get it wrong, you loose a life")






while playerScore != 3 and cpuScore != 3:
    # pass -- Tells Python to skip this block without giving an error.
    secretNumber = random.randint(0, 20) # INCLUSIVE
    print(secretNumber)
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    numGuesses = 0
    for guesses in range(4):
        print(f"You have {4 - numGuesses} guesses remaining.\n")
        playerGuess = int(input("Type a number from 0 to 20 and press ENTER.\n"))
        # input() saves all data as a STRING by default.
        # int() will convert to an INTEGER
        # float() will convert to a FLOAT
        print(f"You have chosen {playerGuess}.  Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("") # PLEASE FINISH             
            playerScore += 1 # IMMEDIATELY EXIT ANY LOOP YOU ARE IN! 
            break # 
        else:
            print("You did not guess correctly.\n")
            if playerGuess > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("The CPU wins a point since you ran out of guesses.\n")

if playerScore >= 3:
    print("Winner, winner, chicken dinner!")
else: 
    # Complete this line with a message that the CPU has won the game.  
    pass 






      

