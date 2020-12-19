file = open("input.txt", "r")
currentMask = []
for line in file:
    splitLine = line.split(' ')
    if splitLine[0] == "mask":
        currentMask.clear()
        for i in range(len(splitLine[2]) - 1):
            currentMask.append(splitLine[2][i])
    else:
        parseNumber = splitLine[0].split('[')[1].split(']')[0]
        print(parseNumber)
print(len(currentMask))
file.close()