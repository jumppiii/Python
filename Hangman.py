# imports
import random

# Array with words
Wordlist = ['apple', 'tomato', 'church', 'sonofabich']

# Attempt counter
Count = 0

# Graveyard for used letters. Graveyard.append(Letter)
Graveyard = []

# Choose random word from array
Word = random.choice(Wordlist)
print(Word)

# Reads input
FirstLetterString = str(input("Enter a letter to start guessing: "))

# Checks if first letter is in the word
if FirstLetterString in Word:
    Graveyard.append(FirstLetterString)
    print(Graveyard)

else:
    print("Not Found")
    Graveyard.append(FirstLetterString)
    Count+1
    print(Graveyard)





