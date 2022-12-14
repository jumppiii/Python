# Loop testing
# for number in range(1000):
#    print(number)
# LetterPosition = []
import os
os.system('cls')
# Array or string that contains the word
mystring = "sonofabich"

# Counts length of word and creates a blank word
LetterLength = len(mystring)
BlankWord = LetterLength * "*"
print("Here's the word: " + BlankWord + "\n")

# Reads input
Letter = str(input("Enter a letter: "))

# Reads position of letters from input and matches with
LetterPosition = ([pos for pos, char in enumerate(mystring) if char == Letter])
# LetterPosition.append([pos for pos, char in enumerate(mystring) if char == Letter])
print(LetterPosition)

for number in LetterPosition:

    BlankWord = BlankWord[:number] + Letter + BlankWord[number+1:]

os.system('cls')
print("Here's the word: " + BlankWord + "\n")
input("Enter a new letter: ")




# LetterPosition.append([pos for pos, char in enumerate(mystring) if char == Letter])
# print(LetterPosition)
# LetterPosition = LetterPosition.astype(int)
