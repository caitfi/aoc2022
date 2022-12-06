f = open("6-input.txt", "r")
buffer = f.readline()

#### part 1 ####
# distinctMeasure = 4

#### part 2 ####
distinctMeasure = 14

for i in range(len(buffer)):
    if i < (distinctMeasure - 1):
        continue
    
    charChunk = [buffer[i]]
    for j in range(1, distinctMeasure):
        charChunk.append(buffer[i-j])
    
    # reverse so you can see the unique characters in order
    charChunk.reverse()

    charChunkSet = set(charChunk)
    if len(charChunk) == len(charChunkSet):
        # all values were unique
        message = "Start of packet at index " + str(i + 1) + ", sequence is " + ''.join(charChunk)
        print(message)
        break