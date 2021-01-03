file = open("input.txt", "r")

current3DSpace = []
new2DSpace = []
for line in file:
    newRow = []
    for i in range(len(line)):
        if line[i] != '\n':
            newRow.append(line[i])
    new2DSpace.append(newRow)
current3DSpace.append(new2DSpace)

# CODE FOR EACH ITERATION - WILL NEED TO PUT IN WHILE LOOP ########

# expand each dimension by one and fill with inactive boxes ('.')
for z in range(len(current3DSpace)):
    for row in range(len(current3DSpace[z])):
        current3DSpace[z][row].append('.')
        current3DSpace[z][row].insert(0, '.')
    newBlankRow = ['.' for x in range(len(current3DSpace[z][0]))]
    current3DSpace[z].append(newBlankRow.copy())
    current3DSpace[z].insert(0, newBlankRow.copy())

new2DList = [['.' for row in range(len(current3DSpace[0]))] for col in range(len(current3DSpace[0][0]))]

current3DSpace.insert(0, new2DList)
current3DSpace.append(new2DList)

# create a copy of the current3DSpace for the next day's 3D space

next3DSpace = [[['.' for x in range(len(current3DSpace[0]))] for y in range(len(current3DSpace[0]))] for z in range(len(current3DSpace))]

for z in range(len(current3DSpace)):
    for y in range(len(current3DSpace[z])):
        for x in range(len(current3DSpace[z][y])):
            currentActiveNeighbors = 0
            if z - 1 >= 0:
                if current3DSpace[z-1][y][x] == '#':
                    currentActiveNeighbors += 1
            if z + 1 < len(current3DSpace):
                if current3DSpace[z+1][y][x] == '#':
                    currentActiveNeighbors += 1
            if x - 1 >= 0:
                if current3DSpace[z][y][x - 1] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y][x - 1] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y][x - 1] == '#':
                        currentActiveNeighbors += 1
            if x - 1 >= 0 and y - 1 >= 0:
                if current3DSpace[z][y-1][x-1] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y - 1][x - 1] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y - 1][x - 1] == '#':
                        currentActiveNeighbors += 1

            if x - 1 >= 0 and y + 1 < len(current3DSpace[z]):
                if current3DSpace[z][y+1][x-1] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y + 1][x - 1] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y + 1][x - 1] == '#':
                        currentActiveNeighbors += 1
            if y - 1 >= 0:
                if current3DSpace[z][y-1][x] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y-1][x] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y-1][x] == '#':
                        currentActiveNeighbors += 1
            if y + 1 < len(current3DSpace[z]):
                if current3DSpace[z][y + 1][x] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y+1][x] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y+1][x] == '#':
                        currentActiveNeighbors += 1
            if x + 1 < len(current3DSpace[z][y]):
                if current3DSpace[z][y][x+1] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y][x+1] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y][x+1] == '#':
                        currentActiveNeighbors += 1
            if x + 1 < len(current3DSpace[z][y]) and y - 1 >= 0:
                if current3DSpace[z][y-1][x+1] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y-1][x+1] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y-1][x+1] == '#':
                        currentActiveNeighbors += 1
            if x + 1 < len(current3DSpace[z][y]) and y + 1 < len(current3DSpace[z]):
                if current3DSpace[z][y+1][x+1] == '#':
                    currentActiveNeighbors += 1
                if z - 1 >= 0:
                    if current3DSpace[z - 1][y + 1][x + 1] == '#':
                        currentActiveNeighbors += 1
                if z + 1 < len(current3DSpace):
                    if current3DSpace[z + 1][y + 1][x + 1] == '#':
                        currentActiveNeighbors += 1

            print(currentActiveNeighbors)
            if current3DSpace[z][y][x] == '#':
                if currentActiveNeighbors == 2 or currentActiveNeighbors == 3:
                    next3DSpace[z][y][x] = '#'
            elif current3DSpace[z][y][x] == '.':
                if currentActiveNeighbors == 3:
                    next3DSpace[z][y][x] = '#'

# set current 3D space to the next day's 3D space

for i in range(len(next3DSpace)):
    for j in range(len(next3DSpace[i])):
        print(next3DSpace[i][j])
    print('')
file.close()
