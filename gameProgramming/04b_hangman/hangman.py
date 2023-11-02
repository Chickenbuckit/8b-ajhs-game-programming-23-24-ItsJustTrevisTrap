# Hangman Game by Trevis Brown, v0.1
import random
words = 'Acid Knife Bones Bleach Reptile Banshee Spirit Spider Snake Disease Skull Photosynthesis Mental Flatline Havoc Yamaha Glove Lime Green Teal Eyes Teeth Cell Blood Phobia Venus Saturn Kawasaki Kill Wendigo'.split()

#VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |    
        |
        |    
    =========''','''
    +---+
    O   |    
        |
        |    
    =========''','''
    +---+
    O   |    
    |   |
        |    
    =========''','''
    +---+
    O   |    
   /|   |
        |    
    =========''','''
    +---+
    O   |    
   /|\  |
        |    
    =========''','''
    +---+
    O   |    
   /|\  |
   /    |    
    =========''','''
    +---+
    O   |    
   /|\  |
   / \  |    
    =========''']

# Pick Word from List
def getRandomWord(wordlist): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()

    blanks = '_' * len(secretWord)
    
    # Replace Blanks with Correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()             

# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1




