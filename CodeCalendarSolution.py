from math import sqrt


def isprime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def great():
    for num in range(100000, 999999):
        # print(num)
        count = 0
        x = num

        for time in range(64):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            num_re = str(num)[::-1]

            num_re = int(num_re)

            if count == 64:
                # print("We counted to 64!")
                if num_re == num:
                    # print("Anna is amazing, but the original number is:")
                    # print(x)
                    # print("The Palindrome is:")
                    # print(num_re)
                    # input("Press enter")

                    if isprime(x):
                        print(x)
                        print("True\n\n")
                    else:
                        y = "x"


great()
# 7,116,342 is the answer
