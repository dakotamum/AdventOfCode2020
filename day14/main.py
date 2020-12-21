# Functions for converting binary to decimal and vice-versa

def decimalToBinary(decimalNumber):
    currentNumber = decimalNumber
    binaryList = []
    for i in range(36):
        if currentNumber >= pow(2, 36 - i - 1):
            binaryList.append('1')
            currentNumber -= pow(2, 36 - i - 1)
        else:
            binaryList.append('0')
    return binaryList
def binaryToDecimal(binaryList):
    decimalNumber = 0
    for i, val in enumerate(binaryList):
        if val == '1':
            decimalNumber += pow(2, len(binaryList) - i - 1)
    return decimalNumber

def floatingBinaryValue(binaryList):
    total = 0
    for i in range(36):
        if binaryList[i] == 'X' or binaryList[i] == '1':
            total += pow(2, len(binaryList) - i - 1)
    return total
##############################################################
##############################################################

file = open("input.txt", "r")

addresses = []
values = []

currentMask = []
for line in file:
    splitLine = line.split(' ')
    if splitLine[0] == "mask":
        currentMask.clear()
        for i in range(len(splitLine[2]) - 1):
            currentMask.append(splitLine[2][i])
    else:
        address = splitLine[0].split('[')[1].split(']')[0]
        number = int(splitLine[2])
        binaryNumber = decimalToBinary(number)

        for j in range(len(binaryNumber)):
            if currentMask[j] == '1' or currentMask[j] == 'X':
                binaryNumber[j] = currentMask[j]


        foundAddress = False
        for k in range(len(addresses)):
            if addresses[k] == address:
                values[k] = floatingBinaryValue(binaryNumber)
                foundAddress = True
        if foundAddress == False:
            addresses.append(address)
            values.append(floatingBinaryValue(binaryNumber))
            
        ''' Part A
        print("current number:\t\t" + str(binaryNumber))
        for j in range(len(binaryNumber)):
            if currentMask[j] == '1' or currentMask[j] == '0':
                binaryNumber[j] = currentMask[j]
        print("mask:\t\t\t" + str(currentMask))
        print("with mask:\t\t " + str(binaryNumber))
        print("with mask:\t\t " + str(binaryToDecimal(binaryNumber)))
        print('')

        foundAddress = False
        for k in range(len(addresses)):
            if addresses[k] == address:
                values[k] = binaryToDecimal(binaryNumber)
                foundAddress = True
        if foundAddress == False:
            addresses.append(address)
            values.append(binaryToDecimal(binaryNumber))
        '''

sum = 0
for i in range(len(values)):
    sum += values[i]

print(sum)

file.close()