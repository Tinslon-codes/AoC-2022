def rangesOverlap(range1, range2):
    n1, n2, n3, n4 = int(range1[0]), int(range2[0]), int(range1[1]), int(range2[1])
    if (n1 <= n4 and n3 >= n2) or (n2 <= n3 and n4 >= n1):
        return 1
    return 0

Data = open("Part 1 data.txt", "r")
total = 0
while True:
    data = Data.readline()
    if data == "":
        break
    data = data.strip("\n")
    data = data.split(",")
    data1 = data[0].split("-")
    data2 = data[1].split("-")
    total += rangesOverlap(data1, data2)

print(total)
