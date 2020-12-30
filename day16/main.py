# read and parse input file ###############################################################################

file = open("input.txt", "r")
entriesAndRanges = {}

for line in file:
    if line == '\n':
        break
    else:
        # read and parse the entries
        entry = line.split(":")[0]
        firstRange = line.split(":")[1].split('or')[0]; secondRange = line.split(":")[1].split('or')[1]
        firstRangeLow = int(firstRange.split("-")[0]); firstRangeHigh = int(firstRange.split("-")[1])
        secondRangeLow = int(secondRange.split("-")[0]); secondRangeHigh = int(secondRange.split("-")[1])

        # add values to dictionary
        entriesAndRanges[entry] = []
        entriesAndRanges[entry].append(firstRangeLow); entriesAndRanges[entry].append(firstRangeHigh)
        entriesAndRanges[entry].append(secondRangeLow); entriesAndRanges[entry].append(secondRangeHigh)
file.readline(); myTicket = file.readline(); file.readline(); file.readline()

###########################################################################################################

numbersOutOfRange = []

for line in file:
    numbers = [int(i) for i in line.split(',')]
    for i in range(len(numbers)):
        foundInRange = False
        for entry in entriesAndRanges:
            if (numbers[i] >= entriesAndRanges[entry][0] and numbers[i] <= entriesAndRanges[entry][1]) or (numbers[i] >= entriesAndRanges[entry][2] and numbers[i] <= entriesAndRanges[entry][3]):
                foundInRange = True
                break
        if foundInRange == False:
            numbersOutOfRange.append(numbers[i])

#print(numbersOutOfRange)
print(sum(numbersOutOfRange))
file.close()