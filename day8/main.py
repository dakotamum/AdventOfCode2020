file = open("input.txt", "r")
steps = []

for line in file:
    dataline = line.split()
    dataline.append('false')
    steps.append(dataline)

revisited = 'false'
accumulation = 0
if len(steps) != 0:
    currentLine = 0
    while revisited == 'false':
        #print("Current line is: " + str(currentLine))
        nextCurrentLine = currentLine + 1
        if steps[currentLine][2] == 'true':
            revisited = 'true'
            #print(str(currentLine) + " was already visited!")
            break
        elif steps[currentLine][0] == 'acc':
            accumulation += int(steps[currentLine][1])
            #print("Adding " + str(steps[currentLine][1]))
        elif steps[currentLine][0] == 'jmp':
            #print("Jumping to line " + str(nextCurrentLine + int(steps[currentLine][1])))
            nextCurrentLine += int(steps[currentLine][1]) - 1
        steps[currentLine][2] = 'true'
        currentLine = nextCurrentLine

print("Value in the accumulator: " + str(accumulation))

file.close()