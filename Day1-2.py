Data = open("Part 1 data.txt", "r")
end = False
caloriesPerElf = []
count = 0
while True:
    data = Data.readline()
    if data == "":
        break
    caloriesPerElf.append(int(data))
    while not end:
        data = Data.readline()
        if data == "\n" or data == "":
            end = True
            count += 1
        else:
            caloriesPerElf[count] += int(data)
    end = False


caloriesPerElf.sort(reverse=True)
total = 0
for i in range(0, 3):
    total += caloriesPerElf[i]
print(total)
