Data = open("Part 1 data.txt", "r")
cycle = 0
x = 1
total = 0
while True:
    data = Data.readline()
    if data == "":
        break
    data = data.strip("\n")
    data = data.split(" ")
    if data[0] == "noop":
        cycle += 1
        if cycle % 20 == 0 and cycle % 40 != 0:
            total += cycle * x
    else:
        for i in range(0, 2):
            cycle += 1
            if cycle % 20 == 0 and cycle % 40 != 0:
                total += cycle * x

        x += int(data[1])

Data.close()
print(total)
