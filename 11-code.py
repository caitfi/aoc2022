import re
import math

dict = {
}

largeMonkeyModulo = 1

with open("11-input.txt", "r") as f:
    lines = f.readlines()
    
    i = 0

    # parse some info about monkeys
    while i < len(lines):
        line = lines[i].strip()
        if len(lines[i].strip()) == 0:
            i += 1
            continue

        # get the number
        monkeyNumber = int(re.split(":|\s+", lines[i].strip())[1]) #ouch

        dict[monkeyNumber] = {}

        # get the starting items
        i += 1
        startingItems = re.split(":|,|\s+",lines[i].strip())
        dict[monkeyNumber]["holdingItems"] = [int(x) for x in startingItems if x.isnumeric()]
        
        # operation can be saved as a string for eval()
        i += 1
        dict[monkeyNumber]["operation"] = lines[i][lines[i].find("=") + 2:].strip()
        
        # test can also be string for eval()
        i += 1
        monkeyModulo = lines[i].strip().split()[-1]
        dict[monkeyNumber]["test"] = "new % " + monkeyModulo + " == 0"

        largeMonkeyModulo *= int(monkeyModulo)
        
        # true and false monkey
        i += 1
        dict[monkeyNumber]["trueMonkey"] = int(lines[i].strip().split()[-1])
        i += 1
        dict[monkeyNumber]["falseMonkey"] = int(lines[i].strip().split()[-1])
        i += 1

monkeyInspections = [0] * len(dict)

# now I have the info, we process the rounds

for round in range(10000):
    for monkey in dict.keys():
        for i in range(len(dict[monkey]["holdingItems"])):
            # inspecting an item
            monkeyInspections[monkey] += 1

            # perform operation
            old = dict[monkey]["holdingItems"][i]
            new = eval(dict[monkey]["operation"])

            # calm down a little bit
            new = new % largeMonkeyModulo

            # evaluate test
            monkeyRecipient = monkey
            testResult = eval(dict[monkey]["test"])

            if (testResult):
                monkeyRecipient = dict[monkey]["trueMonkey"]
            else:
                monkeyRecipient = dict[monkey]["falseMonkey"]
            
            dict[monkeyRecipient]["holdingItems"].append(new)
        
        dict[monkey]["holdingItems"] = []


# get the super-inspecting monkeys
print(monkeyInspections)
monkeyInspections.sort(reverse=True)
totalMonkeyBusiness = monkeyInspections[0] * monkeyInspections[1]

print("Total level of monkey business: {0}".format(totalMonkeyBusiness))
