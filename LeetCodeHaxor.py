import os
import math


def solution():
    num = (int(input("Enter a number: ")))
    output = int(0)

    while not num == 0:
        if (num % 2) == 0:
            num = num / 2
            output += 1
        else:
            num = num - 1
            output += 1
    print(str(output))


def number_hacking():
    count = 0
    os.system("cls")

    value = input("Enter a number that you want to reduce to zero: ")

    while not value.isdigit():
        value = str(input("\nThat's not a number. Try again: "))

    value = int(value)
    value_save = str(value)
    os.system("cls")

    while value != 0:

        if (value % 2) == 0:
            print("\nDividing " + str(value) + " by two..")
            value /= 2
            value = math.trunc(value)
            print("New value = " + str(value))
            count += 1

        else:
            print("\nSubtracting " + str(value) + " by one..")
            value -= 1
            print("New value = " + str(value))
            count += 1

    print("\nIt took " + str(count) + " steps to reduce your number, " + value_save + ", down to zero.")


def main():
    os.system("cls")
    answer = input("Verbose or silent? Answer with V/S: ")
    answer = answer.upper()
    answer = answer[0]

    if answer == "V":
        number_hacking()
    elif answer == "S":
        solution()
    else:
        main()


main()
