def findScenicScore(grid, i1, i2):
    score = 1
    count = 0
    for n in range(0, i1):
        count += 1
        n = i1 - n - 1
        if grid[n][i2] >= grid[i1][i2]:
            break
    score *= count

    count = 0
    for n in range(i1 + 1, len(grid)):
        count += 1
        if grid[n][i2] >= grid[i1][i2]:
            break
    score *= count

    count = 0
    for n in range(0, i2):
        count += 1
        n = i2 - n - 1
        if grid[i1][n] >= grid[i1][i2]:
            break
    score *= count

    count = 0
    for n in range(i2 + 1, len(grid[0])):
        count += 1
        if grid[i1][n] >= grid[i1][i2]:
            break
    score *= count

    return score


Data = open("Part 1 data.txt", "r")
data = Data.read().split("\n")
grid = []
highestScore = 0

for i in range(0, len(data)):
    grid.append([])
    for j in range(0, len(data[i])):
        grid[i].append(data[i][j])

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        newScore = findScenicScore(grid, i, j)
        if newScore > highestScore:
            highestScore = newScore

print(highestScore)
