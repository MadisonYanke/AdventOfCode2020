def getAdjacentSeats(seats, seatRow, seatColumn):
    adjacentSeats = []
    for x in range(seatRow-1, seatRow+2):
        for y in range(seatColumn-1, seatColumn+2):
            if (x == seatRow and y == seatColumn) or (x < 0) or (y < 0): continue
            try:
                adjacentSeats.append(seats[x][y])
            except IndexError:
                continue
    return adjacentSeats

def getVisibleSeat(seats, x, y, xDirection, yDirection):
    visibleSeat = '.'
    while visibleSeat == '.':
        try:
            x += xDirection
            y += yDirection
            if x < 0 or y < 0: break
            visibleSeat = seats[x][y]
        except IndexError:
            break
    return visibleSeat


def getAdjacentVisibleSeats(seats, seatRow, seatColumn):
    adjacentVisibleSeats = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if y == 0 and x == 0: continue
            adjacentVisibleSeats.append(getVisibleSeat(seats, seatRow, seatColumn, x, y))
    return adjacentVisibleSeats

def evaluateGeneration(seats, occupiedThreshold=4, visible=False):
    newSeats = []
    for seatRow in range(len(seats)):
        newRow = ''
        for seatColumn in range(len(seats[0])):
            if visible: adjacentSeats = getAdjacentVisibleSeats(seats, seatRow, seatColumn)
            else: adjacentSeats = getAdjacentSeats(seats, seatRow, seatColumn)
            if seats[seatRow][seatColumn] == 'L':
                countOccupied = adjacentSeats.count('#')
                if countOccupied == 0:
                    newRow += '#'
                else:
                    newRow += 'L'
            elif seats[seatRow][seatColumn] == '#':
                countOccupied = adjacentSeats.count('#')
                if countOccupied >= occupiedThreshold:
                    newRow += 'L'
                else:
                    newRow += '#'
            elif seats[seatRow][seatColumn] == '.':
                newRow += '.'
        newSeats.append(newRow)
    return newSeats


seats = [line.strip() for line in open('day11input.txt')]
consecutiveSameState = 0
oldSeats = seats[:]
while consecutiveSameState < 3:
    newSeats = evaluateGeneration(oldSeats)
    if newSeats == oldSeats:
        consecutiveSameState +=1
    del oldSeats[:]
    oldSeats = newSeats[:]
    del newSeats[:]
occupiedCount = 0
for seatRow in oldSeats:
    occupiedCount += seatRow.count('#')
print(occupiedCount)

consecutiveSameState2 = 0
oldSeats2 = seats[:]
while consecutiveSameState2 < 3:
    newSeats2 = evaluateGeneration(oldSeats2, 5, True)
    if newSeats2 == oldSeats2:
        consecutiveSameState2 +=1
    del oldSeats2[:]
    oldSeats2 = newSeats2[:]
    del newSeats2[:]
occupiedCount2 = 0
for seatRow in oldSeats2:
    occupiedCount2 += seatRow.count('#')
print(occupiedCount2)