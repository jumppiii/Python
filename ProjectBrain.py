import threading


def zero(p, y):
    for num in range(p, y):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def two_five():
    for num in range(250000, 500000):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def five():
    for num in range(500000, 750000):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def seven_five():
    for num in range(750000, 1000000):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def mill(p, y):
    for num in range(p, y):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def mill_two_five():
    for num in range(1250000, 1500000):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def mill_five():
    for num in range(1500000, 1750000):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def mill_seven_five():
    for num in range(1750000, 2000000):
        # print(num)
        count = 0
        x = num

        for time in range(2000):
            count += 1

            num_re = str(num)[::-1]

            num_re = int(num_re)

            num = num + num_re

            if count == 2000:
                # print("We counted to 2000!")
                # print(num)
                # print("\n\n")
                num_str = str(num)

                if num_str[0:4] == "1337":
                    # print("This is the new number")
                    # print(num)
                    # print("This is the original number")
                    print(x)


def main():
    thread1 = threading.Thread(target=zero(0, 250000))
    thread2 = threading.Thread(target=two_five())
    thread3 = threading.Thread(target=five())
    thread4 = threading.Thread(target=seven_five())
    thread5 = threading.Thread(target=mill(1000000, 1250000))
    thread6 = threading.Thread(target=mill_two_five())
    thread7 = threading.Thread(target=mill_five())
    thread8 = threading.Thread(target=mill_seven_five())

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

    print(threading.activeCount())


main()

