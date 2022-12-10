Data = open("Part 1 data.txt", "r")
cycle = 0
x = 1
string = []
for i in range(0, 40):
    string.append(".")
while True:
    data = Data.readline()
    if data == "":
        break
    data = data.strip("\n")
    data = data.split(" ")

    if data[0] == "noop":
        cycle += 1
        thing = (cycle - 1) % 40
        if thing == 0 and cycle > 1:
            string2 = ""
            for i in range(0, len(string)):
                string2 += string[i]
            print(string2)
        char = "."
        if -1 <= (thing - x) <= 1:
            char = "#"
        string[thing] = char

    else:
        for i in range(0, 2):
            cycle += 1
            thing = (cycle - 1) % 40

            if thing == 0 and cycle > 1:
                string2 = ""
                for i in range(0, len(string)):
                    string2 += string[i]
                print(string2)
            char = "."
            if -1 <= thing - x <= 1:
                char = "#"
            string[thing] = char

        x += int(data[1])

Data.close()
string2 = ""
for i in range(0, len(string)):
    string2 += string[i]
print(string2)
