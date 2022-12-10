Data = open("Part 1 data.txt", "r")
headX, headY, tailX, tailY = 0, 0, 0, 0
count = 0
grid = []
for i in range(0, 500):
    grid.append([])
    for j in range(0, 500):
        grid[i].append(0)

while True:
    data = Data.readline()
    if data == "":
        break
    lineData = data.split(" ")
    direction = lineData[0]
    for i in range(0, int(lineData[1])):
        if direction == "U":
            headY += 1
        elif direction == "D":
            headY -= 1
        elif direction == "L":
            headX -= 1
        elif direction == "R":
            headX += 1

        gapX, gapY = headX - tailX, headY - tailY
        if gapX > 1:
            tailX += 1
            tailY = headY
        elif gapX < -1:
            tailX -= 1
            tailY = headY
        elif gapY > 1:
            tailY += 1
            tailX = headX
        elif gapY < -1:
            tailY -= 1
            tailX = headX
        if grid[tailY][tailX] == 0:
            count += 1
            grid[tailY][tailX] = 1

Data.close()
print(count)
