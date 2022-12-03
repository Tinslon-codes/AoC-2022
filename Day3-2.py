def addItemToArray(items, item):
    for i in range(0, len(items)):
        if items[i] == item:
            return
    items.append(item)
    return


def findDuplicateItems(items1, items2):
    duplicateItems = []
    for i in range(0, len(items1)):
        for j in range(0, len(items2)):
            if items1[i] == items2[j]:
                duplicateItems.append(items1[i])
    return duplicateItems


def findAsciiValue(char):
    asciiValue = ord(char)
    if 65 <= asciiValue <= 90:
        priority = asciiValue - 38
    elif asciiValue != 32:
        priority = asciiValue - 96
    else:
        return 10000000
    return priority



Data = open("Part 1 data.txt", "r")
total = 0
end = False
while True:
    data = []
    for i in range(0, 3):
        newLine = Data.readline()
        if newLine == "":
            end = True
            break
        newLine.strip("\n")
        data.append(newLine)
    if end:
        break

    secondList = []
    duplicateItems = findDuplicateItems(data[0], data[1])
    duplicateItem = findDuplicateItems(data[2], duplicateItems)
    priority = findAsciiValue(duplicateItem[0])
    total += priority
    print(duplicateItem, priority)

print(total)

