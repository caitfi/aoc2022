from functools import reduce
import operator

# Goal is a nested dictionary

def fillOutDirectory(linesToCheck):
    directoryDict = {}
    for line in linesToCheck:
        words = line.strip().split(" ")
        # new directory = new dictionary
        if words[0] == "dir":
            directoryDict[words[1]] = {}
        elif words[0].isnumeric():
            directoryDict[words[1]] = int(words[0])

    return directoryDict
            
def getToNestedDictionary(dictionary, recursionList):
    return reduce(operator.getitem, recursionList, dictionary)    

def setValueInNestedDictionary(dictionary, recursionList, value):
    getToNestedDictionary(dictionary, recursionList[:-1])[recursionList[-1]] = value

def printOutDictionary(dictionary):
    directorySum = 0
    smallDirectories = []
    for key, value in dictionary.items():
        if isinstance(value, dict):
            nextDirSum, nextSmall = printOutDictionary(value)
            smallDirectories.extend(nextSmall)
            if nextDirSum < 100000:
                smallDirectories.append(nextDirSum)
            directorySum += nextDirSum
        else:
            directorySum += value
    return directorySum, smallDirectories

f = open("aoc2022/7-input.txt", "r")
lines = f.readlines()

fileSystemDictionary = {
    '/':{}
}

currentDir = ["/"]

i = 1

# skip the cd / because I know I'm there
while i < len(lines):
    line = lines[i]
    words = line.strip().split(" ")
    # if it's a command 
    if words[0] == "$":
        if words[1] == "ls":
            lsLines = []
            i += 1
            # get all non-command lines after this
            while i < len(lines) and "$" not in lines[i]:
                lsLines.append(lines[i])
                i +=1
                
            i -= 1
            # we find out what is in this directory
            thisDirectoryDict = fillOutDirectory(lsLines)
            setValueInNestedDictionary(fileSystemDictionary, currentDir, thisDirectoryDict)
        
        elif words[1] == "cd":
            if words[2].isalpha():
                # I'm in a new directory
                currentDir.append(words[2])
            elif words[2] == "..":
                currentDir.pop()

    i += 1

print("Finished!")
# So now, everything is in a dictionary
# and I have to get the value
totalSum, totalSmall = printOutDictionary(fileSystemDictionary)
print("Total filesystem sum: " + str(totalSum))
print("Sum of small filesystems: " + str(sum(totalSmall)))
