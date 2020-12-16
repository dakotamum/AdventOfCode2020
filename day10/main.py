
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

currentNumberOfInterest = 0
numberOfDifferencesOfOne = 0
numberOfDifferencesOfThree = 1


currentPossibilities = 1


for idx, val in enumerate(sortedAdapters):
    if val - currentNumberOfInterest == 1:
        numberOfDifferencesOfOne += 1
    elif val - currentNumberOfInterest == 3:
        numberOfDifferencesOfThree += 1
    currentNumberOfInterest = val

print("number of differences of one: " + str(numberOfDifferencesOfOne))
print("number of differences of three: " + str(numberOfDifferencesOfThree))
print("number of differences of one * number of differences of three = " + str(numberOfDifferencesOfOne * numberOfDifferencesOfThree))

def tribonnacci(someNumber):
    if someNumber == 0:
        return 0
    elif someNumber == 1:
        return 1
    elif someNumber == 2:
        return 1
    else:
        return tribonnacci(someNumber - 3) + tribonnacci(someNumber - 2) + tribonnacci(someNumber - 1)

currentNumOfOneDiffs = 0
sortedAdapters.insert(0, 0)

for i in range(len(sortedAdapters)-1):
    if sortedAdapters[i+1] - sortedAdapters[i] == 1:
        currentNumOfOneDiffs += 1
    elif sortedAdapters[i+1] - sortedAdapters[i] == 3:
        if currentNumOfOneDiffs > 0:
            currentPossibilities *= tribonnacci(currentNumOfOneDiffs + 1)
            currentNumOfOneDiffs = 0
#print(sortedAdapters)

print(currentPossibilities)

#This was my sort of naive approach to Part B before I realized there was a pattern I could use.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.oneAway = None
        self.twoAway = None
        self.threeAway = None

    def insert(self, data):
        if data - self.data > 3:
            if self.oneAway != None:
                self.oneAway.insert(data)
            if self.twoAway != None:
                self.twoAway.insert(data)
            if self.threeAway != None:
                self.threeAway.insert(data)

        elif data - self.data == 1:
            self.oneAway = Node(data)
        elif data - self.data == 2:
            self.twoAway = Node(data)
            if self.oneAway != None:
                self.oneAway.insert(data)
        elif data - self.data == 3:
            self.threeAway = Node(data)
            if self.oneAway != None:
                self.oneAway.insert(data)
            if self.twoAway != None:
                self.twoAway.insert(data)

    def Printer(self):
        print(self.data)
        if self.oneAway != None:
            self.oneAway.Printer()
        if self.twoAway != None:
            self.twoAway.Printer()
        if self.threeAway != None:
            self.threeAway.Printer()


root = Node(0)

print(sortedAdapters)

for value in sortedAdapters:
    root.insert(int(value))

root.Printer()
'''