with open("aoc2022/10-input.txt") as lines:

    cycle = 1 
    x = 1
    valuesToAdd = []
    cycleCheckValues = [20,60,100,140,180,220]
    checkResults = []
    runningInstruction = False
    instructionFinishes = 0

    pixelToDraw = 0
    modifier = 0

    grid = ['.']*240

    while cycle <= 240:
        # Finish up any instructions due to finish
        if (runningInstruction and instructionFinishes == cycle):
            x += valuesToAdd.pop(0)
            runningInstruction = False
            # print("New x value {0} on cycle {1}".format(x, cycle))

        # if I'm on a particular cycle I want to check
        if cycle in cycleCheckValues:
            result = x * cycle
            print("Value at {0}th cycle is {1}, so result is {2}".format(cycle, x, result))
            checkResults.append(result)

        # if I'm not already doing an instruction, start one
        if (not runningInstruction):
            try:
                line = next(lines)
            except StopIteration:
                break

            words = line.strip().split()
            # addx
            if (words[0] == "addx"):
                valuesToAdd.append(int(words[1]))
                instructionFinishes = cycle + 2
                runningInstruction = True
            
        # draw my grid bit
        # x is the mid sprite position
        # if x-1 or x or x+1 is the pixel I'm on, it's a # - else .
        if (pixelToDraw in [x-1, x, x+1]):
            index = pixelToDraw + (modifier * 40)
            grid[index] = '#'

        if (pixelToDraw == 39):
            pixelToDraw = 0
            modifier += 1
        else:
            pixelToDraw += 1

        cycle += 1


# sum up the results
print("Result sum is {0}".format(sum(checkResults)))

# print my grid properly
prettyGrid = [grid[i:i+40] for i in range(0, len(grid), 40)]
for line in prettyGrid:
    line = ''.join(line)
    print(line)