import random
import os
import base64


def dice_roll():
    flag = "JHtMaXF1aWRBcmVDaG9rZXJzfQ=="
    os.system("cls")
    count = 0

    dice_number = str(input("How many die do you want to roll?\n Enter a number: "))

    while not dice_number.isdigit():
        dice_number = str(input("\n That's not a number. Try again: "))

    dice_number = int(dice_number)

    for i in range(dice_number):
        random_number = random.randint(1, 6)
        count += 1
        count_string = str(count)
        random_number_string = str(random_number)
        print("\nDice " + count_string + " rolled: " + random_number_string)

    if dice_number >= 10000:
        decoded_flag = base64.b64decode(flag).decode('utf-8')
        print("\n Pushing the limits, nice. The flag is: " + decoded_flag)


def try_again():
    tryagain = str(input("\nDo you want to roll the dice again? Y/N: "))
    tryagain = tryagain.upper()
    if tryagain == "N":
        exit()
    elif tryagain == "Y":
        main()
    else:
        try_again()


def main():
    dice_roll()
    try_again()


main()
