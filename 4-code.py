
f = open("4-input.txt", "r")


#### part 1 ####

total = 0

for line in f:
    # split into two ranges
    assignments = line.split(",")
    areaList = []

    for ass in assignments:
        boundaries = ass.split("-")
        areaList.append(range(int(boundaries[0]), int(boundaries[1]) + 1))

    # compare if 0 is a subset of 1, or 1 is a subset of 0
    if (all (x in areaList[0] for x in areaList[1]) or all(x in areaList[1] for x in areaList[0])):
        total += 1

print(total)

f.seek(0)

#### part 2 ####

total = 0

for line in f:
    # split into two ranges
    assignments = line.split(",")
    areaList = []

    for ass in assignments:
        boundaries = ass.split("-")
        areaList.append(range(int(boundaries[0]), int(boundaries[1]) + 1))
    
    # intersection again?
    if set(areaList[0]).intersection(set(areaList[1])):
        total += 1

print(total)

f.close()