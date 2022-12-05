f = open("5-input.txt","r")
lines = f.readlines()

emptyChar = '0'

i = 0

# ideally this could dynamically add more rows.. but for now I'll be basic
# get the initial structure
i = lines.index("\n")

letterPoints = []
instructionStart = i + 1

i -= 1
numberAlignment = lines[i]
# first line to check is the numbers
# can use this to find the points where letters would be
for index, character in enumerate(numberAlignment):
    if character.isnumeric():
        letterPoints.append(index)

k = 0
i -= 1
grid = [[] for i in range(len(letterPoints))]

# then rewind back and add to the grid (upside down)
while i >= 0:
    j = 0

    for index in letterPoints:
        currentCharacter = lines[i][index]
        if currentCharacter.isalpha():
            grid[j].append(currentCharacter)
        j += 1

    i -= 1

# OK - now I actually have my grid
for i in range (instructionStart, len(lines)):
    # parse the instructions
    words = lines[i].strip().split(" ")

    boxesToMove = int(words[1])
    originPile = int(words[3]) - 1
    destPile = int(words[5]) - 1
    
    groupToMove = []

    while boxesToMove > 0:
        topCrate = grid[originPile].pop()

        #### part 1 ####
        # grid[destPile].append(topCrate)

        #### part 2 ####
        groupToMove.append(topCrate)
        
        boxesToMove -= 1
    
    ### part 2 ###
    while len(groupToMove) > 0:
        nextCrate = groupToMove.pop()
        grid[destPile].append(nextCrate)
    
topCrates = []
for column in grid:
    topCrates.append(column[-1])

print(''.join(topCrates))
    

    



