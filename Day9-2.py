Data = open("Part 1 data.txt", "r")
count = 0
numNodes = 10
nodes = []
for i in range(0, numNodes):
    nodes.append([500, 500])
grid = []
for i in range(0, 1000):
    grid.append([])
    for j in range(0, 1000):
        grid[i].append(0)

while True:
    data = Data.readline()
    if data == "":
        break
    lineData = data.split(" ")
    direction = lineData[0]
    for m in range(0, int(lineData[1])):
        if direction == "U":
            nodes[0][1] += 1
        elif direction == "D":
            nodes[0][1] -= 1
        elif direction == "L":
            nodes[0][0] -= 1
        elif direction == "R":
            nodes[0][0] += 1

        for i in range(0, numNodes - 1):
            i2 = i + 1
            gapX, gapY = nodes[i][0] - nodes[i2][0], nodes[i][1] - nodes[i2][1]
            if gapX > 1:
                nodes[i2][0] += 1
                if gapY >= 1:
                    nodes[i2][1] += 1
                elif gapY <= -1:
                    nodes[i2][1] -= 1

            elif gapX < -1:
                nodes[i2][0] -= 1
                if gapY >= 1:
                    nodes[i2][1] += 1
                elif gapY <= -1:
                    nodes[i2][1] -= 1

            elif gapY > 1:
                nodes[i2][1] += 1
                if gapX >= 1:
                    nodes[i2][0] += 1
                elif gapX <= -1:
                    nodes[i2][0] -= 1

            elif gapY < -1:
                nodes[i2][1] -= 1
                if gapX >= 1:
                    nodes[i2][0] += 1
                elif gapX <= -1:
                    nodes[i2][0] -= 1

        tailCoords = nodes[numNodes-1]
        if grid[tailCoords[0]][tailCoords[1]] == 0:
            count += 1
            grid[tailCoords[0]][tailCoords[1]] = 1

Data.close()
print(count)
