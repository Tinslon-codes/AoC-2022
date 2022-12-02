Data = open("Part 1 data.txt", "r")
pointsForOutcome = {"X": 0, "Y": 3, "Z": 6}
pointsForMove = {"A": 1, "B": 2, "C": 3}
score = 0
while True:
    data = Data.readline()
    if data == "":
        break
    data = data.strip("\n")
    round = data.split(" ")
    a, b = round[0], round[1]
    if b == "X":
        pointThing = -1
    elif b == "Y":
        pointThing = 0
    else:
        pointThing = 1
    score += ((pointsForMove[a]+pointThing-1) % 3) + 1
    score += pointsForOutcome[b]
print(score)
