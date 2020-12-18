file = open("input.txt", "r")
strings = []

for line in file:
    strings.append(line)

startingTime = int(strings[0])
values = strings[1].split(',')
#print(startingTime)
#print(values)
smallestWaitTime = int(values[0]) - (startingTime % int(values[0]))
smallestID = values[0]

for i, val in enumerate(values):
    if val != 'x':
        if (int(val) - (startingTime % int(val))) < smallestWaitTime:
            smallestWaitTime = (int(val) - (startingTime % int(val)))    
            smallestID = int(val)

print(smallestID * smallestWaitTime)

file.close()