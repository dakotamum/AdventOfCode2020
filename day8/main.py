file = open("input.txt", "r")
steps = []
nop_or_jmp_indices = []

#get indices of nop or jmp
current_nop_or_jump_index = 0
for line in file:
    dataline = line.split()
    dataline.append('false')
    steps.append(dataline)
    if dataline[0] == 'nop' or dataline[0] == 'jmp':
        nop_or_jmp_indices.append(current_nop_or_jump_index)
    current_nop_or_jump_index += 1

accumulation = 0
current_nop_or_jmp = 0;
foundValidSet = 'false'

#print(nop_or_jmp_indices)
#print("Original steps array: ")
#for line in steps:
#    print(line)

#perform a trial run for each nop or jmp instruction that exists
for i in range(len(nop_or_jmp_indices)):
    #reset stats for each trial
    accumulation = 0
    revisited = 'false'

    # switch a nop to a jmp or vice-versa
    if steps[nop_or_jmp_indices[i]][0] == 'jmp':
        steps[nop_or_jmp_indices[i]][0] = 'nop'
    elif steps[nop_or_jmp_indices[i]][0] == 'nop':
        steps[nop_or_jmp_indices[i]][0] = 'jmp'

    #reset steps array for each trial
    for index in range(len(steps)):
        steps[index][2] = 'false'

    #print("")
    #print("a steps array: ")
    #print("")

    #for line in steps:
    #    print(line)

    ##### PART A
    if len(steps) != 0:
        currentLine = 0
        while revisited == 'false':
            nextCurrentLine = currentLine + 1
            if currentLine >= len(steps):
                #the current line has reached the end and indicates a valid run
                foundValidSet = 'true'
                break
            elif steps[currentLine][2] == 'true':
                revisited = 'true'
                break
            elif steps[currentLine][0] == 'acc':
                accumulation += int(steps[currentLine][1])
            elif steps[currentLine][0] == 'jmp':
                nextCurrentLine += int(steps[currentLine][1]) - 1
            steps[currentLine][2] = 'true'
            currentLine = nextCurrentLine
    #############
        #print(accumulation)
    if foundValidSet == 'true':
        break
    #change the nop back to jmp or vice versa for the next run
    if steps[nop_or_jmp_indices[i]][0] == 'jmp':
        steps[nop_or_jmp_indices[i]][0] = 'nop'
    elif steps[nop_or_jmp_indices[i]][0] == 'nop':
        steps[nop_or_jmp_indices[i]][0] = 'jmp'

print("Value in the accumulator: " + str(accumulation))

file.close()