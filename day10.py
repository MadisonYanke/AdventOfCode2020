import itertools as it
import math

def Mult1And3JoltJumps(adapters):
    joltJumps1 = 0
    joltJumps3 = 1
    if (min(adapters) == 1): joltJumps1 += 1
    elif (min(adapters) == 3): joltJumps3 += 1
    for x in range(1, len(adapters)):
        if abs(adapters[x] - adapters[x-1]) == 1: joltJumps1 += 1
        elif abs(adapters[x] - adapters[x-1]) == 3: joltJumps3 += 1
    return joltJumps1 * joltJumps3

def getJoltDifferences(adapters):
    joltDifs = [min(adapters)]
    for x in range(1, len(adapters)):
        joltDifs.append(abs(adapters[x] - adapters[x-1]))
    joltDifs.append(3)
    return joltDifs

def getRemovableIndices(adapters):
    joltsDifs = getJoltDifferences(adapters)
    removableIndices = []
    for x in range(0, len(adapters)):
        if joltsDifs[x] + joltsDifs[x+1] <= 3:
            removableIndices.append(x)
    return removableIndices

def validateCombination(combo, lowerBound, upperBound):
    chain = combo[:]
    chain = [lowerBound] + chain + [upperBound]
    for x in range(1, len(chain)):
        if chain[x] - chain[x-1] > 3:
            return False
    return True

def findCombinationsForSet(comboSet, lowerBound, upperBound):
    numberOfValidCombos = 0
    print(comboSet)
    if lowerBound > upperBound: lowerBound = 0
    for x in range(0, len(comboSet)):
        for y in it.combinations(comboSet, x+1):
            if validateCombination(list(y), lowerBound, upperBound): numberOfValidCombos += 1
    if validateCombination([], lowerBound, upperBound): numberOfValidCombos += 1
    return numberOfValidCombos


adapters = [int(line.strip()) for line in open('day10input.txt')]
adapters.sort()
print(Mult1And3JoltJumps(adapters))
removableIndices = getRemovableIndices(adapters)
sets = []
tempSet = [removableIndices[0]]
for x in range(1, len(removableIndices)):
    if removableIndices[x] - removableIndices[x-1] == 1:
        tempSet.append(removableIndices[x])
    else:
        sets.append(tempSet[:])
        del tempSet[:]
        tempSet.append(removableIndices[x])
sets.append(tempSet)

combosPerSet = []
for comboSet in sets:
    testSet = []
    for combo in comboSet:
        testSet.append(adapters[combo])
    combosPerSet.append(findCombinationsForSet(testSet, adapters[min(comboSet)-1], adapters[max(comboSet)+1]))
    del testSet[:]

print(adapters)
print(combosPerSet)
print(math.prod(combosPerSet))