def findSeatId(boardingPass):
    rowBinary = boardingPass[0:7]
    columnBinary = boardingPass[7:]
    rowBinary = rowBinary.replace('F', '0').replace('B','1')
    columnBinary = columnBinary.replace('L', '0').replace('R', '1')
    row = int(rowBinary, 2)
    column = int(columnBinary, 2)
    return (8*row+column)

def findMissingPasses(seatIds, totalSeats):
    missingSeats = []
    for seat in range(totalSeats):
        if seat not in seatIds:
            missingSeats.append(seat)
    return missingSeats

def findSantasSeat(missingSeats, seatIds):
    for missingSeat in missingSeats:
        if missingSeat-1 in seatIds and missingSeat+1 in seatIds:
            return missingSeat


boardingPasses = [line.strip() for line in open('day5input.txt')]
max = 0
seatIds = []
for boardingPass in boardingPasses:
    seatId = findSeatId(boardingPass)
    seatIds.append(seatId)
    if seatId > max:
        max = seatId
totalSeats = 128 * 8

print(max)
print(findSantasSeat(findMissingPasses(seatIds, totalSeats), seatIds))
