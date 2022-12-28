file = open("numbers.txt", "r")

count = 0

for line in file:
    first_elf = line[:line.index(",")]
    first_elf_first_room = first_elf.split("-")[0]
    first_elf_second_room = first_elf.split("-")[1]
    # print(first_elf_first_room)
    # print(first_elf_second_room)
    # print(first_elf)

    second_elf = line[line.index(",")::]
    second_elf = second_elf.split(",")[1]
    second_elf_first_room = second_elf.split("-")[0]
    second_elf_second_room = second_elf.split("-")[1]
    # print("gon be 96", second_elf_second_room)

    a = int(first_elf_first_room)
    b = int(first_elf_second_room)
    x = int(second_elf_first_room)
    y = int(second_elf_second_room)

    if a >= x and b <= y:
        count += 1
        print(first_elf, second_elf)

    elif x >= a and y <= b:
        count += 1
        print(first_elf, second_elf)

    else:
        for num in range(a, b):
            if num == x or y:
                count += 1
                continue

print("Count:", count)
