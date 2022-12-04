def addItemToArray(items, item):
    for i in range(0, len(items)):
        if items[i] == item:
            return
    items.append(item)
    return


def findDuplicateItem(items1, items2):
    for i in range(0, len(items1)):
        for j in range(0, len(items2)):
            if items1[i] == items2[j]:
                return items1[i]
    return " "


Data = open("Part 1 data.txt", "r")
total = 0
while True:
    data = Data.readline()
    if data == "":
        break
    data = data.strip("\n")

    numItems = int(len(data)/2)
    comp1Items, comp2Items = [], []
    for i in range(0, numItems):
        addItemToArray(comp1Items, data[i])
    for i in range(numItems, (numItems*2)):
        addItemToArray(comp2Items, data[i])

    duplicateItem = findDuplicateItem(comp1Items, comp2Items)
    asciiValue = ord(duplicateItem)
    if 65 <= asciiValue <= 90:
        priority = asciiValue - 38
    elif asciiValue != 32:
        priority = asciiValue - 96
    else:
        break
    total += priority

print(total)
