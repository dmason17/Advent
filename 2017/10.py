list = [0,1,2,3,4]
input = [3, 4]
skip = 0
index = 0
for x in input:
    endIndex = index + x
    subList = []
    for y in range(0, len(list)):
        if y < endIndex and y >= index :
            subList.append(list[y])
        else:
            subList.append(0)
    for y in range(index, endIndex):
        list[y] = subList[endIndex-1-y]
    index += x + skip
    index = index % len(list)
    skip += 1

print skip
print index
print list
print subList
