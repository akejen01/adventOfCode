# Day
# 5# coding=utf-8


def calculateRow(entry):
    entry = entry.replace('F', '0')
    entry = entry.replace('B', '1')
    return int(entry, 2)


def calculateColumn(entry):
    entry = entry.replace('L', '0')
    entry = entry.replace('R', '1')
    return int(entry, 2)



with open('Day5_input.txt') as f:
    entries = f.read().splitlines()
f.close()

maxSeatID = 0

for entry in entries:
    currentRow = calculateRow(entry[:7])
    currentColumn = calculateColumn(entry[7:])
    currentSeatID = currentRow * 8 + currentColumn
    print('Row: {0}, column: {1} , SeatID : {2}'.format(currentRow, currentColumn, currentSeatID))

    if ( currentSeatID > maxSeatID):
        maxSeatID = currentSeatID

print(maxSeatID)



