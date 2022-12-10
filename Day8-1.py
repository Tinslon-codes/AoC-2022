def isTreeVisible(grid, i1, i2):
    visible = True
    for n in range(0, i1):
        if grid[n][i2] >= grid[i1][i2]:
            visible = False
            break
    if visible:
        return True

    visible = True
    for n in range(i1 + 1, len(grid)):
        if grid[n][i2] >= grid[i1][i2]:
            visible = False
            break
    if visible:
        return True

    visible = True
    for n in range(0, i2):
        if grid[i1][n] >= grid[i1][i2]:
            visible = False
            break
    if visible:
        return True

    visible = True
    for n in range(i2 + 1, len(grid[0])):
        if grid[i1][n] >= grid[i1][i2]:
            visible = False
            break
    if visible:
        return True

    return False


Data = open("Part 1 data.txt", "r")
data = Data.read().split("\n")
grid = []

for i in range(0, len(data)):
    grid.append([])
    for j in range(0, len(data[i])):
        grid[i].append(data[i][j])

treesVisible = (len(grid) + len(grid[0]) - 2) * 2

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if isTreeVisible(grid, i, j):
            treesVisible += 1

print(treesVisible)
