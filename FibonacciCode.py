import os


# function that creates the fibonacci sequence, pulled in main()
def fibonacci_game():
    n1 = 0
    n2 = 1
    count = 0
    lines = int(input("Enter how many lines of fibonacci code you want: "))

# while the counter is less than lines, continue printing the sequence
    while count < lines:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# function for endgame / retry
def try_again():
    tryagain = str(input("\nDo you want to generate a new fibonacci string? Y/N: "))
    tryagain = tryagain.upper()
    if tryagain == "N":
        exit()
    elif tryagain == "Y":
        main()
    else:
        try_again()


# function for the program that gets run
def main():
    os.system("cls")
    fibonacci_game()
    try_again()


# runs main() function
main()
