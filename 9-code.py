def catchUpToNextKnot(hPos, tPos):
    visitedSpaces = {tuple(tPos)}
    if (abs(tPos[0] - hPos[0]) > 1 or abs(tPos[1] - hPos[1]) > 1):
        # if they are in a line
        if (hPos[0] == tPos[0] or hPos[1] == tPos[1]):
            shiftIndex = 1 if hPos[0] == tPos[0] else 0

            if (hPos[shiftIndex] > tPos[shiftIndex]):
                tPos[shiftIndex] += 1
                
            elif (hPos[shiftIndex] < tPos[shiftIndex]):
                tPos[shiftIndex] -= 1

            visitedSpaces.add(tuple(tPos))

        # if they are diagonally distant
        else:
            xShift = +1 if (hPos[1] > tPos[1]) else -1
            yShift = +1 if (hPos[0] > tPos[0]) else -1
            tPos[1] += xShift
            tPos[0] += yShift
            visitedSpaces.add(tuple(tPos))
    
    return tPos, visitedSpaces

f = open("aoc2022/9-input.txt", "r")
lines = f.readlines()

ropeLength = 10

knotList = [[0,0] for i in range(ropeLength)]
tailVisited = {(0,0)}

for line in lines:
    instructions = line.strip().split()
    
    direction = instructions[0]
    distance = int(instructions[1])

    for i in range(distance):
        match(direction):
            case 'R':
                knotList[0][1] += 1
            case 'L':
                knotList[0][1] -= 1
            case 'U':
                knotList[0][0] += 1
            case 'D':
                knotList[0][0] -= 1

        for i in range(1, ropeLength):
            newKnotPos, knotsVisited = catchUpToNextKnot(knotList[i-1], knotList[i])
            
            # if this is the last knot
            if i == ropeLength - 1:
                tailVisited.update(knotsVisited)

print("Tail visited {0} coordinates".format(len(tailVisited)))

f.close()