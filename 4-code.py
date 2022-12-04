
f = open("4-input.txt", "r")


#### part 1 AND 2 ####

subset = 0
overlap = 0

for line in f:
    # split into two ranges
    assignments = line.split(",")
    areaList = []

    for ass in assignments:
        boundaries = ass.split("-")
        areaList.append(range(int(boundaries[0]), int(boundaries[1]) + 1))

    # compare if 0 is a subset of 1, or 1 is a subset of 0
    if (all (x in areaList[0] for x in areaList[1]) or all(x in areaList[1] for x in areaList[0])):
        subset += 1
    
    # intersection again?
    if set(areaList[0]).intersection(set(areaList[1])):
        overlap += 1

print(subset)
print(overlap)

f.close()