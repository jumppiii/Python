matches = open("ABC.txt", "r")

rock = 1
paper = 2
scissors = 3

loss = 0
draw = 3
win = 6

score = 0

for match in matches:
    enemy = match[0]
    me = match[2]

    if enemy == "A" and me == "X":
        score += draw
        score += rock

    elif enemy == "A" and me == "Y":
        score += win
        score += paper

    elif enemy == "A" and me == "Z":
        score += loss
        score += scissors

    elif enemy == "B" and me == "X":
        score += loss
        score += rock

    elif enemy == "B" and me == "Y":
        score += draw
        score += paper

    elif enemy == "B" and me == "Z":
        score += win
        score += scissors

    elif enemy == "C" and me == "X":
        score += win
        score += rock

    elif enemy == "C" and me == "Y":
        score += loss
        score += paper

    elif enemy == "C" and me == "Z":
        score += draw
        score += scissors

print(score)
