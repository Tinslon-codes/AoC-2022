Data = open("Part 1 data.txt", "r")
pointsForMove = {"X": 1, "Y": 2, "Z": 3}
score = 0
while True:
    data = Data.readline()
    if data == "":
        break
    data = data.strip("\n")
    round = data.split(" ")
    a, b = round[0], round[1]
    if (a=="A" and b=="X") or (a=="B" and b=="Y") or (a=="C" and b=="Z"):
        score += 3
    elif (a=="A" and b=="Z") or (a=="B" and b=="X") or (a=="C" and b=="Y"):
        score += 0
    else:
        score += 6
    score += pointsForMove[b]
print(score)
