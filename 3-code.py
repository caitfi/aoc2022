from itertools import islice

def getPriority(character):
    priority = 0

    if (character.isupper()):
        # 'A' = ascii 65 - I want start at 27
        priority = ord(character) - ord('A') + 27
        
    elif (character.islower()):
        # 'a' = ascii 97 - should be 1
        priority = ord(character) - ord('a') + 1
    
    return(priority)

f = open("3-input.txt", "r")

totalPriorities = 0

#### part 1 ####
for line in f:

    # split line in half
    middle = len(line) // 2
    firstHalf = set(line[:middle])
    secondHalf = set(line[middle:])

    # find common character in each set
    result = firstHalf.intersection(secondHalf)
    result = list(result)[0]

    # get priority of the character 
    priority = getPriority(result)

    totalPriorities += priority

print(totalPriorities)
f.seek(0)

#### part 2 ####
totalPriorities = 0
nextThreeLines = []
count = 1

for index, line in enumerate(f):
    # iterate through 3 lines at once 
    if (count < 3):
        betterLine = line[:-1]
        nextThreeLines.append(betterLine)
        count += 1
        continue
    elif (count == 3):
        betterLine = line[:-1]
        nextThreeLines.append(betterLine)
        count = 1
        # convert to sets and get intersection 
        result = list(set(nextThreeLines[0]).intersection(set(nextThreeLines[1]), set(nextThreeLines[2])))
        result = result[0]

        # priorities again
        priority = getPriority(result)
        totalPriorities += priority
        nextThreeLines = []

print(totalPriorities)