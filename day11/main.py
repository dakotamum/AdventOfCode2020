'''
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

Your puzzle answer was 2194.

--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 1944.
'''

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
                #Part A
                '''
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
                '''

                # Part B

                # check upperleft
                upperleft = 1
                while(True):
                    if i - upperleft >= 0 and j - upperleft >= 0:
                        if fairyRows[i - upperleft][j - upperleft] == 'L':
                            break
                        elif fairyRows[i - upperleft][j - upperleft] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        upperleft += 1
                    else:
                        break

                # check upper
                upper = 1
                while(True):
                    if i - upper >= 0:
                        if fairyRows[i - upper][j] == 'L':
                            break
                        elif fairyRows[i - upper][j] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        upper += 1
                    else:
                        break

                # check upperright
                upperright = 1
                while(True):
                    if i - upperright >= 0 and j + upperright < len(fairyRows[i]):
                        if fairyRows[i - upperright][j + upperright] == 'L':
                            break
                        elif fairyRows[i - upperright][j + upperright] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        upperright += 1
                    else:
                        break

                # check right
                right = 1
                while(True):
                    if j + right < len(fairyRows[i]):
                        if fairyRows[i][j + right] == 'L':
                            break
                        elif fairyRows[i][j + right] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        right += 1
                    else:
                        break

                # check lowerright
                lowerright = 1
                while(True):
                    if i + lowerright < len(fairyRows) and j + lowerright < len(fairyRows[i]):
                        if fairyRows[i + lowerright][j + lowerright] == 'L':
                            break
                        elif fairyRows[i + lowerright][j + lowerright] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        lowerright += 1
                    else:
                        break

                # check lower
                lower = 1
                while(True):
                    if i + lower < len(fairyRows):
                        if fairyRows[i + lower][j] == 'L':
                            break
                        elif fairyRows[i + lower][j] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        lower += 1
                    else:
                        break

                # check lowerleft
                lowerleft = 1
                while(True):
                    if i + lowerleft < len(fairyRows) and j - lowerleft >= 0:
                        if fairyRows[i + lowerleft][j - lowerleft] == 'L':
                            break
                        elif fairyRows[i + lowerleft][j - lowerleft] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        lowerleft += 1
                    else:
                        break

                # check left
                left = 1
                while(True):
                    if j - left >= 0:
                        if fairyRows[i][j - left] == 'L':
                            break
                        elif fairyRows[i][j - left] == '#':
                            adjacentOccupiedSeats += 1
                            break
                        left += 1
                    else:
                        break

                if fairyRows[i][j] == 'L':
                    if adjacentOccupiedSeats == 0:
                        fairyRowsTomorrow[i][j] = '#'
                        madeChange = True
                elif fairyRows[i][j] == '#':
                    stableUnoccupiedSeats += 1
                    if adjacentOccupiedSeats >= 5:
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

file.close()