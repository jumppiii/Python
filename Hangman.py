# imports
import random
import os

# Graveyard for used letters. Graveyard.append(Letter)
Graveyard = []

# New letter function

def new_letter():

    os.system("cls")
    print(Word)
    print("Here's the word: " + BlankWord + "\n")
    LetterString = str(input("Enter a letter to start guessing: "))
    print("\n\n")
    str(Graveyard.append(LetterString))
    graveyardstring =' '
    for letters in Graveyard:
        graveyardstring += ' ' + letters
    print("Purgatory: " + graveyardstring)


# Clear screen
os.system("cls")

# Array with words
Wordlist = ['apple', 'tomato', 'church', 'sonofabich']

# Attempt counter
Count = 0

# Choose random word from array
Word = random.choice(Wordlist)
print(Word)

# Creates the BlankWord
LetterLength = len(Word)
BlankWord = LetterLength * "*"

# Prints the blank word
print("Here's the word: " + BlankWord + "\n")

# Reads input
# LetterString = str(input("Enter a letter to start guessing: "))

# Starts a while loop
while BlankWord != Word:
    LetterString = "test"
    new_letter()

    if LetterString in Word:
        LetterPosition = ([pos for pos, char in enumerate(Word) if char == LetterString])
        for number in LetterPosition:
            BlankWord = BlankWord[:number] + LetterString + BlankWord[number + 1:]
            print(BlankWord)
        #    print("Here's the word: " + BlankWord + "\n")
        #    LetterString = input("Enter a new letter: ")
        #    print("\n\n\n" + Graveyard)

    else:
        print("Not Found")
        Graveyard.append(LetterString)
        Count + 1
        print(Graveyard)





