count = 0
repeatCounter = 0
colAList = []
colBList = []
colCList = []
finalList = []


def isNotValidTriangle(a, b, c):
    if int(a) + int(b) <= int(c):
        return True

def checkAllTriangles(a, b, c):
    if isNotValidTriangle(a, b, c) or isNotValidTriangle(a, c, b) or isNotValidTriangle(b, a, c) or isNotValidTriangle(b, c, a) or isNotValidTriangle(c, a, b) or isNotValidTriangle(c, b, a):
        return True


f = open('3.txt', 'r')
for line in f:
    lineSplit = line.split()
    if(repeatCounter > 2):
        finalList.append(colAList[0] + " " + colAList[1] + " " + colAList[2])
        finalList.append(colBList[0] + " " + colBList[1] + " " + colBList[2])
        finalList.append(colCList[0] + " " + colCList[1] + " " + colCList[2])
        colAList = []
        colBList = []
        colCList = []
        repeatCounter = 0

    colAList.append(lineSplit[0])
    colBList.append(lineSplit[1])
    colCList.append(lineSplit[2])
    repeatCounter = repeatCounter + 1
    if checkAllTriangles(lineSplit[0], lineSplit[1], lineSplit[2]):
        continue
    count = count + 1

f.close();
finalList.append(colAList[0] + " " + colAList[1] + " " + colAList[2])
finalList.append(colBList[0] + " " + colBList[1] + " " + colBList[2])
finalList.append(colCList[0] + " " + colCList[1] + " " + colCList[2])


print count

count = 0
for x in finalList:
    lineSplit = x.split()
    if checkAllTriangles(lineSplit[0], lineSplit[1], lineSplit[2]):
        continue
    count = count + 1

print count
