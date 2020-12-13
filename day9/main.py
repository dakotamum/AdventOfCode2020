def validateNumber(numberInQuestion, numberList):
    isGood = 'false'
    for i in range(len(numberList)):
        for j in range(len(numberList)):
            if numberInQuestion == numberList[i] + numberList[j]:
                isGood = 'true'
                break
        if isGood == 'true':
            break
    return isGood

file = open("input.txt", "r")
numbers = []

for line in file:
    numbers.append(int(line))

print(numbers)

preamble = 5

currentNumberArray = []

for currentNumberIndex in range(5):
    currentNumberArray.append(numbers[currentNumberIndex])

print("current number array: ")
print(currentNumberArray)

for i in range(preamble, len(numbers)):
    print(numbers[i])

print(validateNumber(numbers[preamble], numbers))