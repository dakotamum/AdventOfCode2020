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

#print(numbers)

preamble = 25
currentNumberArray = []

for currentNumberIndex in range(preamble):
    currentNumberArray.append(numbers[currentNumberIndex])

#print("current number array: ")
#print(currentNumberArray)

#for i in range(preamble, len(numbers)):
#    print(numbers[i])

#print(validateNumber(numbers[preamble], numbers))

numberThatDoesntAddUp = 0

for iter in range(preamble, len(numbers)):
    if validateNumber(numbers[iter], currentNumberArray) == 'false':
        numberThatDoesntAddUp = numbers[iter]
        break
    else:
        currentNumberArray.pop(0)
        currentNumberArray.append(numbers[iter])

print("Number that doesn't add up: " + str(numberThatDoesntAddUp))