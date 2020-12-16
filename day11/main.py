file = open("input.txt", "r")

fairyRows = []
fairyRowsTomorrow = []

for line in file:
    aRow = []
    for i in range(len(line)):
        if line[i] != '\n':
            aRow.append(line[i])
    fairyRows.append(aRow)

# make copy of fairyRows for fairyRowsTomorrow 2D list
for i in range(len(fairyRows)):
    anotherRow = []
    for j in range(len(fairyRows[i])):
        anotherRow.append(fairyRows[i][j])
    fairyRowsTomorrow.append(anotherRow)

stableUnoccupiedSeats = 0
madeChange = True

while madeChange == True:
    madeChange = False
    stableUnoccupiedSeats = 0
    for i in range(len(fairyRows)):
        for j in range(len(fairyRows[i])):
            adjacentOccupiedSeats = 0
            if fairyRows[i][j] != '.':
                if i - 1 >= 0 and j - 1 >= 0:
                    if fairyRows[i - 1][j - 1] == '#':
                        adjacentOccupiedSeats += 1
                if i - 1 >= 0:
                    if fairyRows[i - 1][j] == '#':
                        adjacentOccupiedSeats += 1
                if i - 1 >= 0 and j + 1 < len(fairyRows[i]):
                    if fairyRows[i - 1][j + 1] == '#':
                        adjacentOccupiedSeats += 1
                if j + 1 < len(fairyRows[i]):
                    if fairyRows[i][j + 1] == '#':
                        adjacentOccupiedSeats += 1
                if i + 1 < len(fairyRows) and j + 1 < len(fairyRows[i]):
                    if fairyRows[i + 1][j + 1] == '#':
                        adjacentOccupiedSeats += 1
                if i + 1 < len(fairyRows):
                    if fairyRows[i + 1][j] == '#':
                        adjacentOccupiedSeats += 1
                if i + 1 < len(fairyRows) and j - 1 >= 0:
                    if fairyRows[i + 1][j - 1] == '#':
                        adjacentOccupiedSeats += 1
                if j - 1 >= 0:
                    if fairyRows[i][j - 1] == '#':
                        adjacentOccupiedSeats += 1

                if fairyRows[i][j] == 'L':
                    if adjacentOccupiedSeats == 0:
                        fairyRowsTomorrow[i][j] = '#'
                        madeChange = True
                elif fairyRows[i][j] == '#':
                    stableUnoccupiedSeats += 1
                    if adjacentOccupiedSeats >= 4:
                        fairyRowsTomorrow[i][j] = 'L'
                        madeChange = True

            #print(fairyRows[i][j], end='') 
        #print('\n', end='')
    #print("")

    if madeChange == True:
        for i in range(len(fairyRowsTomorrow)):
            for j in range(len(fairyRowsTomorrow[i])):
                fairyRows[i][j] = fairyRowsTomorrow[i][j]

print("Stable occupied seats: " + str(stableUnoccupiedSeats))
