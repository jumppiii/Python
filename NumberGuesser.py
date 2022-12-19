count = 0

for i in range(1000):
    if i % 3 == 0 and i % 5 != 0:
        print("True")
        count = count + 1

    else:
        print("Not True")

print(count)
