import itertools as it

def findFlawedNumber(numbers, loadedSize=25):
    previousNums = numbers[:loadedSize]
    print(previousNums)
    for x in range(loadedSize, len(numbers)):
        anyTwoSum = [sum(combo) for combo in it.combinations(previousNums, 2)]
        if numbers[x] in anyTwoSum:
            previousNums = numbers[(x+1)-loadedSize:(x+1)]
        else:
            return numbers[x]
    return None

def findContiguousNumbers(numbers, sumNum):
    contiguousList = []
    for x in range(len(numbers)):
        for y in range(x, len(numbers)):
            contiguousList.append(numbers[y])
            if sum(contiguousList) == sumNum:
                return contiguousList
            elif sum(contiguousList) > sumNum:
                del contiguousList[:]
                break

inputNumbers = [int(line.strip()) for line in open('day9input.txt')]

flawedNumber = findFlawedNumber(inputNumbers)
print(flawedNumber)
contiguousNumbers = findContiguousNumbers(inputNumbers, flawedNumber)
print(min(contiguousNumbers) + max(contiguousNumbers))

