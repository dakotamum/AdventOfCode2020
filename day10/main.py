file = open("input.txt", "r")

sortedAdapters = []

for line in file:
    indexToInsert = 0
    for idx, val in enumerate(sortedAdapters):
        if int(line) >= val:
            indexToInsert += 1
        elif int(line) < val:
            break
    sortedAdapters.insert(indexToInsert, int(line))

print(sortedAdapters)

currentNumberOfInterest = 0
numberOfDifferencesOfOne = 0
numberOfDifferencesOfThree = 1

for idx, val in enumerate(sortedAdapters):
    if val - currentNumberOfInterest == 1:
        numberOfDifferencesOfOne += 1
    elif val - currentNumberOfInterest == 3:
        numberOfDifferencesOfThree += 1
    currentNumberOfInterest = val

print("number of differences of one: " + str(numberOfDifferencesOfOne))
print("number of differences of three: " + str(numberOfDifferencesOfThree))
print("number of differences of one * number of differences of three = " + str(numberOfDifferencesOfOne * numberOfDifferencesOfThree))