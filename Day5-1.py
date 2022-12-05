def findNumStacks(Data):
    i = 0
    while True:
        line = Data.readline()
        if line[1] == "1":
            return int((len(line) + 2)/4), i
        i += 1


def addDataToStacks(stacks, Data, endLine):
    Data.seek(0)
    allData = Data.read().split("\n")
    for i in range(0, endLine):
        i = (endLine - i) - 1
        data = allData[i]
        numStacksOnLine = int((len(data) + 1)/4)
        for i in range(0, numStacksOnLine):
            newData = data[(i * 4) + 1]
            if newData != " ":
                stacks[i].append(newData)


Data = open("Part 1 data.txt", "r")
numStacks, endOfStacksLine = findNumStacks(Data)
stacks = []
instructions = False

for thing in range(0, numStacks):
    stacks.append([])

addDataToStacks(stacks, Data, endOfStacksLine)

Data.seek(0)
while True:
    line = Data.readline()
    if line == "":
        break
    elif instructions or line[0] == "m":
        instructions = True

    if instructions:
        line = line.strip("\n")
        lineData = line.split(" ")
        for thing in range(0, int(lineData[1])):
            if len(stacks[int(lineData[3]) - 1]) > 0:
                var = stacks[int(lineData[3]) - 1].pop()
                stacks[int(lineData[5]) - 1].append(var)

string = ""
for i in range(0, len(stacks)):
    if len(stacks[i]) > 0:
        string += str(stacks[i][len(stacks[i]) - 1])
    else:
        string += " "

print(string)
