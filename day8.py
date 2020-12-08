def tryRunProgram(instructions):
    accumulator = 0
    hasInstructionRan = [False for x in instructions]
    instructionIter = 0
    while True:
        try:
            if hasInstructionRan[instructionIter]: return [accumulator, hasInstructionRan]
            if instructions[instructionIter][0] == 'nop':
                hasInstructionRan[instructionIter] = True
                instructionIter += 1
            elif instructions[instructionIter][0] == 'acc':
                hasInstructionRan[instructionIter] = True
                accumulator += int(instructions[instructionIter][1])
                instructionIter += 1
            elif instructions[instructionIter][0] == 'jmp':
                hasInstructionRan[instructionIter] = True
                instructionIter += int(instructions[instructionIter][1])
        except IndexError:
            if instructionIter == len(instructions): return [accumulator, None]



instructions = [(line.split()[0], line.split()[1]) for line in open('day8input.txt')]
results = tryRunProgram(instructions)
print(results[0])

for x in range(len(results[1])):
    if results[1][x]:
        newInstructions = instructions[:]
        if instructions[x][0] == 'nop':
            newInstructions[x] = ('jmp', instructions[x][1])
        elif instructions[x][0] == 'jmp':
            newInstructions[x] = ('nop', instructions[x][1])
        didProgramComplete = tryRunProgram(newInstructions)
        if didProgramComplete[1] == None:
            print(didProgramComplete[0])
            break