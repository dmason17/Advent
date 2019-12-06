# startingBlocks = [0,2,7,0]
startingBlocks = [2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]
memory = []

def allocate(blocks):
    highestNum = 0
    i = 0
    for x in range(0, len(blocks)):
        if blocks[x] > highestNum:
            highestNum = blocks[x]
            i = x
    amountToReallocate = blocks[i]
    blocks[i] = 0
    if i == len(blocks)-1:
        i = 0
    else:
        i += 1
    while amountToReallocate > 0:
        blocks[i] += 1
        amountToReallocate-=1
        if i == len(blocks)-1:
            i = 0
        else:
            i += 1

    for x in range(0, len(memory)):
        if str(memory[x]) == str(blocks):
            return x - 1
    memory.append(list(blocks))
    return 0

counter = 0
keepGoing = 0
print "Calculating"
while keepGoing == 0:
    keepGoing = allocate(startingBlocks)
    counter += 1
print "1: " + str(counter)
print "2: " + str(counter - keepGoing)
