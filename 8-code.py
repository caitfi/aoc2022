import numpy as np

def checkVisibleDirection(grid, index, currentValue, isXdirection):
    lineToCheck =  grid[index[0], :] if isXdirection else  grid[:, index[1]]
    currentIndex = index[1] if isXdirection else index[0]

    isVisibleNegative = True
    isVisiblePositive = True

    closestNeg = 0
    closestPos = len(lineToCheck) - 1
    foundClosestPos = False

    for idx, value in np.ndenumerate(lineToCheck):
        if idx[0] == currentIndex:
            continue 
        elif idx[0] < currentIndex and value >= currentValue:
            isVisibleNegative = False
            closestNeg = idx[0]
        elif idx[0] > currentIndex and value >= currentValue:
            isVisiblePositive = False
            if (not foundClosestPos):
                closestPos = idx[0]
                foundClosestPos = True

    isVisible = isVisibleNegative or isVisiblePositive
    scenicScore = (currentIndex - closestNeg) * (closestPos - currentIndex)
    return isVisible, scenicScore

f = open("aoc2022/8-input.txt", "r")
lines = f.readlines()

grid = np.zeros((len(lines), len(lines[0].strip())))

for i, line in enumerate(lines):
    betterLine = line.strip()
    for j, chara in enumerate(betterLine):
        grid[i,j] = chara

totalVisible = 0
maxScenicScore = 0
bestScenicIndex = None

for index, value in np.ndenumerate(grid):
    # if around the edge, automatically visible
    if (index[0] == 0 or index[0] == (grid.shape[0] - 1) or index[1] == 0 or index[1] == (grid.shape[1] - 1)):
        totalVisible += 1
    else:
        # x direction
        isVisibleX, xScenicScore = checkVisibleDirection(grid, index, value, True)
        # if not visible on x, check y
        isVisibleY, yScenicScore = checkVisibleDirection(grid, index, value, False)

        isVisible = isVisibleX or isVisibleY
        scenicScore = xScenicScore * yScenicScore
        # if visible in any direction, increment
        if (isVisible):
            totalVisible += 1
        
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore
            bestScenicIndex = index

print("Total visible trees from all directions: {0}".format(totalVisible))
print("Best possible scenic score is {0} at location {1}".format(maxScenicScore, bestScenicIndex))
f.close()