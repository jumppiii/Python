for num in range(1000000, 2000000):
    count = 0
    x = num

    for time in range(2000):
        count += 1  # adds 1 to the counter

        num_store = num  # stores new num value

        num_re = str(num)[::-1]  # creates num_re string from num

        num_re = int(num_re)  # converts num_re to integer

        num = num + num_re  # adds num_re and num to create the new iteration

        # print(x)
        # print(num)

        if num_store == num_re:
            # print(num_store)
            # print(num_re)
            # print("Continuing..")
            break

        if count == 2000:
            # print("We counted to 2000!")
            # print(x)
            # print("\n\n")
            num_str = str(num)

            if num_str[0:4] == "1337":
                # print("This is the new number")
                # print(num)
                print("This is the original number")
                print(x)
