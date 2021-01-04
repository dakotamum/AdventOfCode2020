file = open("input.txt", "r")

current4DSpace = []
new3DSpace = []
new2DSpace = []
for line in file:
    newRow = []
    for i in range(len(line)):
        if line[i] != '\n':
            newRow.append(line[i])
    new2DSpace.append(newRow)
new3DSpace.append(new2DSpace)
current4DSpace.append(new3DSpace)

print(current4DSpace)
next4DSpace = []

for i in range(6):

    # expand each dimension by one and fill with inactive boxes ('.')
    for w in range (len(current4DSpace)):
        for z in range(len(current4DSpace[w])):
            for row in range(len(current4DSpace[w][z])):
                current4DSpace[w][z][row].append('.')
                current4DSpace[w][z][row].insert(0, '.')
            newBlankRow = ['.' for x in range(len(current4DSpace[w][z][0]))]
            current4DSpace[w][z].append(newBlankRow.copy())
            current4DSpace[w][z].insert(0, newBlankRow.copy())

    new3DList = [[['.' for sheet in range(len(current4DSpace[0]))] for row in range(len(current4DSpace[0][0]))] for col in range(len(current4DSpace[0][0][0]))]

    current4DSpace.insert(0, new3DList)
    current4DSpace.append(new3DList)

    # create a copy of the current4DSpace for the next day's 4D space

    next4DSpace = [[[['.' for x in range(len(current4DSpace[0][0]))] for y in range(len(current4DSpace[0][0]))] for z in range(len(current4DSpace[0]))] for w in range(len(current4DSpace))]

    for w in range(len(current4DSpace)):
        for z in range(len(current4DSpace)):
            for y in range(len(current4DSpace[w][z])):
                for x in range(len(current4DSpace[w][z][y])):
                    currentActiveNeighbors = 0
                    if w - 1 >= 0:
                        if current4DSpace[w-1][z][y][x] == '#':
                            currentActiveNeighbors += 1
                    if w + 1 < len(current4DSpace):
                        if current4DSpace[w+1][z][y][x] == '#':
                            currentActiveNeighbors += 1
                    if z - 1 >= 0:
                        if current4DSpace[w][z-1][y][x] == '#':
                            currentActiveNeighbors += 1
                        if w - 1 >= 0:
                            if current4DSpace[w-1][z-1][y][x] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w+1][z-1][y][x] == '#':
                                currentActiveNeighbors += 1
                    if z + 1 < len(current4DSpace[w]):
                        if current4DSpace[w][z+1][y][x] == '#':
                            currentActiveNeighbors += 1
                        if w - 1 >= 0:
                            if current4DSpace[w-1][z+1][y][x] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w+1][z+1][y][x] == '#':
                                currentActiveNeighbors += 1

                    if x - 1 >= 0:
                        if current4DSpace[w][z][y][x - 1] == '#':
                            currentActiveNeighbors += 1
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y][x-1] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y][x-1] == '#':
                                currentActiveNeighbors += 1

                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y][x - 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y][x-1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y][x-1] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y][x - 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y][x-1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y][x-1] == '#':
                                    currentActiveNeighbors += 1

                    if x - 1 >= 0 and y - 1 >= 0:
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y-1][x-1] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y-1][x-1] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y-1][x-1] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y - 1][x - 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y-1][x-1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y-1][x-1] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y - 1][x - 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y-1][x-1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y-1][x-1] == '#':
                                    currentActiveNeighbors += 1

                    if x - 1 >= 0 and y + 1 < len(current4DSpace[w][z]):
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y+1][x-1] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y+1][x-1] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y+1][x-1] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y + 1][x - 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y+1][x-1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y+1][x-1] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y + 1][x - 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y+1][x-1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y+1][x-1] == '#':
                                    currentActiveNeighbors += 1

                    if y - 1 >= 0:
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y-1][x] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y-1][x] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y-1][x] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y-1][x] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y-1][x] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y-1][x] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y-1][x] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y-1][x] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y-1][x] == '#':
                                    currentActiveNeighbors += 1

                    if y + 1 < len(current4DSpace[w][z]):
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y+1][x] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y+1][x] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y + 1][x] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y+1][x] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y+1][x] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y+1][x] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y+1][x] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y+1][x] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y+1][x] == '#':
                                    currentActiveNeighbors += 1

                    if x + 1 < len(current4DSpace[w][z][y]):
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y][x+1] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y][x+1] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y][x+1] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y][x+1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y][x+1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y][x+1] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y][x+1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y][x+1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y][x+1] == '#':
                                    currentActiveNeighbors += 1

                    if x + 1 < len(current4DSpace[w][z][y]) and y - 1 >= 0:
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y-1][x+1] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y-1][x+1] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y-1][x+1] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y-1][x+1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y-1][x+1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y-1][x+1] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y-1][x+1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y-1][x+1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y-1][x+1] == '#':
                                    currentActiveNeighbors += 1

                    if x + 1 < len(current4DSpace[w][z][y]) and y + 1 < len(current4DSpace[w][z]):
                        if w - 1 >= 0:
                            if current4DSpace[w - 1][z][y+1][x+1] == '#':
                                currentActiveNeighbors += 1
                        if w + 1 < len(current4DSpace):
                            if current4DSpace[w + 1][z][y+1][x+1] == '#':
                                currentActiveNeighbors += 1
                        if current4DSpace[w][z][y+1][x+1] == '#':
                            currentActiveNeighbors += 1
                        if z - 1 >= 0:
                            if current4DSpace[w][z - 1][y + 1][x + 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z-1][y+1][x+1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z-1][y+1][x+1] == '#':
                                    currentActiveNeighbors += 1
                        if z + 1 < len(current4DSpace[w]):
                            if current4DSpace[w][z + 1][y + 1][x + 1] == '#':
                                currentActiveNeighbors += 1
                            if w - 1 >= 0:
                                if current4DSpace[w - 1][z+1][y+1][x+1] == '#':
                                    currentActiveNeighbors += 1
                            if w + 1 < len(current4DSpace):
                                if current4DSpace[w + 1][z+1][y+1][x+1] == '#':
                                    currentActiveNeighbors += 1

                    if current4DSpace[w][z][y][x] == '#':
                        if currentActiveNeighbors == 2 or currentActiveNeighbors == 3:
                            next4DSpace[w][z][y][x] = '#'
                    elif current4DSpace[w][z][y][x] == '.':
                        if currentActiveNeighbors == 3:
                            next4DSpace[w][z][y][x] = '#'
    current4DSpace = next4DSpace

'''
for i in range(len(next3DSpace)):
    for j in range(len(next3DSpace[i])):
        print(next3DSpace[i][j])
    print('')
'''

# count number of active cubes
numberOfActiveCubes = 0
for w in range(len(current4DSpace)):
    for i in range(len(current4DSpace[w])):
        for j in range(len(current4DSpace[w][i])):
            for k in range(len(current4DSpace[w][i][j])):
                if current4DSpace[w][i][j][k] == '#':
                    numberOfActiveCubes += 1

print('number of active cubes: ' + str(numberOfActiveCubes))

file.close()
