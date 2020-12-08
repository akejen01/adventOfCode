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
listOfIDs = []

for entry in entries:
    currentRow = calculateRow(entry[:7])
    currentColumn = calculateColumn(entry[7:])
    currentSeatID = currentRow * 8 + currentColumn
    print('Row: {0}, column: {1} , SeatID : {2}'.format(currentRow, currentColumn, currentSeatID))
    listOfIDs.append(currentSeatID)

    if ( currentSeatID > maxSeatID):
        maxSeatID = currentSeatID

listOfIDs.sort()

for i in range(len(listOfIDs)):
    print(listOfIDs[i])
    if(listOfIDs[i] + 1 != listOfIDs[i+1]):
        print("Häpp")






