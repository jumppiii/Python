def great():
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


great()
# 7,116,342 is the answer
