
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

''' PART A
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
'''

#Part B

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
'''
root.insert(1)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(10)
root.insert(11)
root.insert(12)
root.insert(15)
root.insert(16)
root.insert(19)
'''

root.Printer()