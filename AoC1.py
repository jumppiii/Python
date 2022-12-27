def get_total():
    numbers = open('numbers.txt', 'r')  # opens number file

    result = open("results.txt", "w")

    num = 0  # sets variable

    for line in numbers:  # for line in the numbers file
        line = int(line.strip() or 0)  # strips line or sets it to 0

        if line == 0:  # if line == 0, write the added numbers to results.txt and reset variable "num"
            # print(num)
            result.write(str(num))
            result.write("\n")
            num = 0

        else:  # if line != 0, add line + num together
            num += line

    numbers.close()
    result.close()


def get_biggest_number():
    res = open("results.txt", "r")

    num = 0

    for number in res:
        res_num = int(number)
        if num < res_num:
            num = res_num

    print("\nHere's the largest number:", num)
    res.close()


def get_top_three():
    res = open("results.txt", "r")

    num_list = []

    count = 0

    for number in res:
        num_list.append(int(number))

    num_list.sort()
    num_list.reverse()

    for rank in range(3):
        count += 1
        print("Rank", count, num_list[rank])


get_total()
get_biggest_number()
get_top_three()
