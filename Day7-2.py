def recursiveFunc():
    global data
    global totalSize
    global line
    global maxLine
    global fileSizes
    fileSize = 0
    returnOut = False

    while True:
        dataLine = data[line]
        if dataLine == "":
            return fileSize
        dataLine = dataLine.split(" ")
        if dataLine[1] == "cd":
            line += 1
            if dataLine[2] == "..":
                returnOut = True
            else:
                fileSize += recursiveFunc()
                if line >= maxLine:
                    returnOut = True

            if returnOut:
                fileSizes.append(fileSize)
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
                    totalSize += int(dataLine[0])


global totalSize
global fileSizes
global data
global line
global maxLine
Data = open("Part 1 data.txt", "r")
data = Data.read().split("\n")
line = 0
maxLine = len(data) - 1
fileSizes = []
totalSize = 0

recursiveFunc()

fileSizes.sort()
dir = 0
for i in range(0, len(fileSizes)):
    if fileSizes[i] >= totalSize - 40000000:
        dir = fileSizes[i]
        break
print(dir)
