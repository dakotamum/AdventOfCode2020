file = open("input.txt", "r")

numbersAlreadyMentioned = [int(i) for i in file.readline().split(',')]
indicesOfNumbersAlreadyMentioned = []
for i in range(len(numbersAlreadyMentioned)):
    indicesOfNumbersAlreadyMentioned.append(i + 1)

currentIteration = len(indicesOfNumbersAlreadyMentioned)
lastNumber = 0
while currentIteration <= 2020:
    lastNumber = numbersAlreadyMentioned[currentIteration - 1]
    #print(lastNumber)
    foundAnotherLastNumber = False    
    index = 0
    #print('')
    #print("Printing an iteration...")
    #print(str(numbersAlreadyMentioned))
    #print('current iteration = ' + str(currentIteration))
    #print('last number = ' + str(lastNumber))
    for i in reversed(range(len(numbersAlreadyMentioned) - 1)):
        #print(numbersAlreadyMentioned[i])
        #print('comparing ' + str(numbersAlreadyMentioned[i]) + ' with ' + str(lastNumber) + ' at index ' + str(currentIteration - i - 1))
        if numbersAlreadyMentioned[i] == lastNumber:
            foundAnotherLastNumber = True
            #print('found match ' + str(currentIteration - i - 1) + ' away')
            numbersAlreadyMentioned.append(currentIteration - i - 1)
            #print(str(numbersAlreadyMentioned))
            #del numbersAlreadyMentioned[i]
            break
    if foundAnotherLastNumber == False:
        numbersAlreadyMentioned.append(0)
    if currentIteration % 1000000 == 0:
        print(currentIteration)
    currentIteration += 1
print(lastNumber)
file.close()