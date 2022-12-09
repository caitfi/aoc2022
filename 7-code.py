from functools import reduce
import operator
import sys

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

def unrollDictionary(dictionary, currentPath=''):
    originalPath = currentPath
    directorySum = 0
    smallDirectories = []
    allDirectories = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            if len(currentPath) < 1:
                currentPath = currentPath + key
            else:
                currentPath = currentPath + key + '/'
            nextDirSum, nextSmall, nextAll = unrollDictionary(value, currentPath)

            smallDirectories.extend(nextSmall)
            allDirectories.update(nextAll)

            allDirectories[currentPath] = nextDirSum
            if nextDirSum < 100000:
                smallDirectories.append(nextDirSum)

            directorySum += nextDirSum
        else:
            directorySum += value
        currentPath = originalPath

    
    return directorySum, smallDirectories, allDirectories

f = open("aoc2022/7-input.txt", "r")
lines = f.readlines()

fileSystemDictionary = {
    '/':{}
}

currentDir = ["/"]
listedDirs = []

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
totalSum, totalSmall, totalAll = unrollDictionary(fileSystemDictionary)
print("Total filesystem sum: " + str(totalSum))
print("Sum of small filesystems: " + str(sum(totalSmall)))

# the amount of space I need
neededSpace = 30000000 - (70000000 - totalSum)
print("Space needed: " + str(neededSpace))

largeEnoughDirs = dict([(key,val) for key,val in totalAll.items() if val >= neededSpace])
print(largeEnoughDirs)

dirToDelete = min(largeEnoughDirs, key=largeEnoughDirs.get)
print("Directory to delete is {0}, with size {1}".format(dirToDelete, largeEnoughDirs[dirToDelete]))
