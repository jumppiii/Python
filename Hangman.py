import random
import os
import base64


def display_hangman(count):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[count]


EncodedFlag = "JHtBbGNoZW15T2ZTb3VscyF9"

Graveyard = []

count = 6

Wordlist = ['apple', 'tomato', 'church', 'keyboard', 'mouse', 'internet', 'pokemon', 'korea', 'browser', 'programming',
            'gaming', 'screen', 'phonebook',
            'wallet', 'eternity', 'tattoo', 'painting', 'driving', 'porsche', 'mercedes', 'switch', 'playstation',
            'javascript', 'dictionary', 'hacking',
            'pattern', 'thought', 'breeze', 'sunshine', 'psycho', 'sonofabich']

Word = random.choice(Wordlist)

LetterLength = len(Word)
BlankWord = LetterLength * "*"

while BlankWord != Word:
    if count > 0:
        os.system("cls")
        countStr = str(count)
        print("Lives left: " + countStr + "\n\n")
        GraveyardString =''

        for letters in Graveyard:
            GraveyardString += ' ' + letters

        print("Purgatory:" + GraveyardString)
        print("\n\nHere's the word: " + BlankWord + "\n")
        print(display_hangman(count))
        LetterString = str(input("\nEnter a letter: "))
        LetterString = LetterString.lower()
        LetterString = LetterString[0]
        while LetterString in GraveyardString:
            LetterString = str(input("\nYou've already tried that, enter a new letter: "))
            LetterString = LetterString.lower()
            LetterString = LetterString[0]
        print("\n\n")
        str(Graveyard.append(LetterString))

        if LetterString in Word:
            LetterPosition = ([pos for pos, char in enumerate(Word) if char == LetterString])
            for number in LetterPosition:
                BlankWord = BlankWord[:number] + LetterString + BlankWord[number + 1:]

        else:
            count = count - 1
    else:
        break

if count >= 4:
    os.system("cls")
    DecodedFlag = base64.b64decode(EncodedFlag).decode('utf-8')
    print("You've unlocked the secret flag!\n\nHere's your flag: " + DecodedFlag)
    input("\nPress ENTER to continue..")

elif count > 0:
    os.system("cls")
    print("Congratulations, you solved the hangman with " + countStr + " lives left! The word was: " + Word + "\n")
    print("Solve it with a maximum of 2 mistakes to unlock the secret")
    input("\nPress ENTER to continue..")

elif count >= 0:
    os.system("cls")
    print("You died, the word was: " + Word + ".")
    input("\nPress ENTER to continue..")
