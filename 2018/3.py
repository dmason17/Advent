def printMat(matrix):
    for x in range(0,8):
        print matrix[x]

def xCount(matrix):
    count = 0
    for x in range(0,1000):
        for y in range(0,1000):
            if mat[x][y] == 'X':
                count += 1
    return count


mat = []
for x in range(0,1000):
    row = []
    for y in range(0,1000):
        row.append('.')
    mat.append(row)

idList = []
f = open('3.txt', 'r')
for line in f:
    lineSplit = line.split()
    id = lineSplit[0].replace('#', '')
    idList.append(id)
    coor = lineSplit[2].replace(':', '')
    size = lineSplit[3]
    for x in range(int(coor.split(',')[1]), int(coor.split(',')[1])+int(size.split('x')[1])):
        for y in range(int(coor.split(',')[0]), int(coor.split(',')[0])+int(size.split('x')[0])):
            if mat[x][y] != '.':
                removeMe = mat[x][y]
                mat[x][y] = 'X'
                try:
                    idList.remove(id)
                except:
                    pass
                try:
                    idList.remove(removeMe)
                except:
                    pass

            else:
                mat[x][y] = id
f.close();
# printMat(mat)
print '1: ' + str(xCount(mat))
print idList
