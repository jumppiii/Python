import random
import os
import base64

EncodedFlag = "JHtBbGNoZW15T2ZTb3VscyF9"

Graveyard = []

Wordlist = ['apple', 'tomato', 'church', 'keyboard', 'mouse', 'internet', 'pokemon', 'korea', 'browser', 'programming', 'gaming', 'screen', 'phonebook',
            'wallet', 'eternity', 'tattoo', 'painting', 'driving', 'porsche', 'mercedes', 'switch', 'playstation', 'javascript', 'dictionary', 'hacking',
            'pattern', 'thought', 'breeze', 'sunshine', 'psycho', 'sonofabich']

Count = 0

Word = random.choice(Wordlist)

LetterLength = len(Word)
BlankWord = LetterLength * "*"

while BlankWord != Word:
    if Count < 10:
        os.system("clear")
        CountStr = str(Count)
        print("Attempt(s): " + CountStr + "\n\n")
        GraveyardString =''

        for letters in Graveyard:
            GraveyardString += ' ' + letters

        print("Purgatory:" + GraveyardString)
        print("\n\nHere's the word: " + BlankWord + "\n")
        LetterString = str(input("\nEnter a letter: "))
        print("\n\n")
        str(Graveyard.append(LetterString))

        if LetterString in Word:
            LetterPosition = ([pos for pos, char in enumerate(Word) if char == LetterString])
            for number in LetterPosition:
                BlankWord = BlankWord[:number] + LetterString + BlankWord[number + 1:]

        else:
            Count = Count + 1
    else:
        break


if Count <= 2:
    os.system("clear")
    DecodedFlag = base64.b64decode(EncodedFlag).decode('utf-8')
    print("You've unlocked the secret flag!\n\nHere's your flag: " + DecodedFlag)
    input("\nPress ENTER to continue..")

elif Count < 10:
    os.system("clear")
    print("Congratulations, you solved the hangman in " + CountStr + " attempt(s)!\n")
    print("Solve it with a maximum of 2 mistakes to unlock the secret")
    input("\nPress ENTER to continue..")

elif Count >= 10:
    os.system("clear")
    print("You died, the word was " + Word + ".")
    input("\nPress ENTER to continue..")
