'''
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

Your puzzle answer was 23954.

--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

Your puzzle answer was 453459307723.
'''

# could probably clean up a bit, but it works
# read and parse input file ###############################################################################

file = open("input.txt", "r")
entriesAndRanges = {}

for line in file:
    if line == '\n':
        break
    else:
        # read and parse the entries
        entry = line.split(":")[0]
        firstRange = line.split(":")[1].split('or')[0]; secondRange = line.split(":")[1].split('or')[1]
        firstRangeLow = int(firstRange.split("-")[0]); firstRangeHigh = int(firstRange.split("-")[1])
        secondRangeLow = int(secondRange.split("-")[0]); secondRangeHigh = int(secondRange.split("-")[1])

        # add values to dictionary
        entriesAndRanges[entry] = []
        entriesAndRanges[entry].append(firstRangeLow); entriesAndRanges[entry].append(firstRangeHigh)
        entriesAndRanges[entry].append(secondRangeLow); entriesAndRanges[entry].append(secondRangeHigh)
file.readline(); myTicket = file.readline(); file.readline(); file.readline()
myTicketNumbers = [int(i) for i in myTicket.split(',')]

# add valid tickets to list and initialize possibilities list  #################################################################################################

validTickets = []
for line in file:
    numbers = [int(i) for i in line.split(',')]
    isValid = True
    for i in range(len(numbers)):
        foundInRange = False
        for entry in entriesAndRanges:
            if (numbers[i] >= entriesAndRanges[entry][0] and numbers[i] <= entriesAndRanges[entry][1]) or (numbers[i] >= entriesAndRanges[entry][2] and numbers[i] <= entriesAndRanges[entry][3]):
                foundInRange = True
                break
        if foundInRange == False:
            isValid = False
            break
    if isValid == True:
        validTickets.append(numbers)

possibilities = []
for key in entriesAndRanges:
    possibilities.append(key)
currentPossiblities = possibilities.copy()
possibilitiesByColumn = []

# discover all possibilities by column ##############################################################################################################

for i in range(len(possibilities)):
    myPossibilities = currentPossiblities.copy()
    # for each value in the column 
    for row in validTickets:
        for j in range(len(myPossibilities)):
            if myPossibilities[j] in entriesAndRanges:
                if (row[i] < entriesAndRanges[myPossibilities[j]][0] or row[i] > entriesAndRanges[myPossibilities[j]][1]) and (row[i] < entriesAndRanges[myPossibilities[j]][2] or row[i] > entriesAndRanges[myPossibilities[j]][3]):
                    myPossibilities[j] = '***'
    theColumnEntryForMe = ''
    potentialValues = []
    for text in myPossibilities:
        if text != '***':
            theColumnEntryForMe = text
            potentialValues.append(text)
    possibilitiesByColumn.append(potentialValues)

entriesAndColumnPositions = {}

# go through each column's possibilities narrow each column to one entry ###########################################################################
madeDeletions = True
while madeDeletions == True:
    madeDeletions = False
    for i in range(len(possibilitiesByColumn)):
        if len(possibilitiesByColumn[i]) == 1:
            entriesAndColumnPositions[possibilitiesByColumn[i][0]] = i
            wordToDelete = possibilitiesByColumn[i][0]
            for j in range(len(possibilitiesByColumn)):
                if wordToDelete in possibilitiesByColumn[j]:
                    possibilitiesByColumn[j].remove(wordToDelete)
            madeDeletions = True

productOfDepartures = 1
for entry in entriesAndColumnPositions:
    if entry.find('departure') != -1:
        productOfDepartures *= myTicketNumbers[entriesAndColumnPositions[entry]]

print('product of departure entries for my ticket: ' + str(productOfDepartures))

file.close()