input = open("1-input.txt", "r")

sum = 0
max = 0
totalCals = []

for line in input:
    cals = 0
    if (line == '\n'):
        totalCals.append(sum)
    
        sum = 0
    else:
        cals = int(line)
        sum += cals

totalCals.sort(reverse = True)

total = totalCals[0] + totalCals[1] + totalCals[2]
print(total)