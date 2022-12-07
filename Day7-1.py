def recursiveFunc():
    global data
    global total
    global line
    global maxLine
    fileSize = 0

    while True:
        dataLine = data[line]
        if dataLine == "":
            return fileSize
        dataLine = dataLine.split(" ")
        if dataLine[1] == "cd":
            line += 1
            if dataLine[2] == "..":
                if fileSize <= 100000:
                    total += fileSize
                return fileSize
            else:
                fileSize += recursiveFunc()
                if line >= maxLine:
                    if fileSize <= 100000:
                        total += fileSize
                    return fileSize

        elif dataLine[1] == "ls":
            while True:
                line += 1
                if line > maxLine:
                    return fileSize
                dataLine = data[line].split(" ")
                if dataLine[0] == "$":
                    break
                elif dataLine[0] != "dir":
                    fileSize += int(dataLine[0])


global total
global data
global line
global maxLine
Data = open("Part 1 data.txt", "r")
data = Data.read().split("\n")
total = 0
line = 0
maxLine = len(data) - 1

recursiveFunc()
print(total)
