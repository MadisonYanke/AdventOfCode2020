def TreesBonked(forest, horizontalMovement, verticalMovement = 1):
    vertForest = forest[::verticalMovement]
    treesBonked = 0
    horizontalPosition = 0
    rowLength = len(vertForest[0])
    for row in vertForest:
        if row[horizontalPosition % rowLength] == '#':
            treesBonked += 1
        horizontalPosition += horizontalMovement
    return treesBonked

forest = [line.strip() for line in open('day3input.txt')]

slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2],
]

result = 1
for slope in slopes:
    result *= TreesBonked(forest, slope[0], slope[1])
    
print TreesBonked(forest, 3, 1)
print result
