# 278
num = 23
root = 0
for x in range(0, 1000):
    if (1+ 2 * x) * (1 +2 *x) < num:
        root = x

root = 1
x = root
a = (1 + 2 * x) * (1 + 2 * x)
b = (1 + 2 * (x+1)) * (1 + 2 * (x+1))
c = (1 + 2 * (x+1)) * (1 + 2 * (x+1))- (1 + 2 * x) * (1 + 2 * x)
d = (1 + 2 * (x+1)) -1
e = x+1
# print "1: " + str(e +abs(d/2 - (num - a)%d))
# print "2: "


def test(x, y, matrix):
    sum = 0
    sum += matrix[x+1][y]
    sum += matrix[x+1][y+1]
    sum += matrix[x][y+1]
    sum += matrix[x-1][y+1]
    sum += matrix[x-1][y]
    sum += matrix[x-1][y-1]
    sum += matrix[x][y-1]
    sum += matrix[x+1][y-1]
    return sum

def add(base, num, mat):
    for x in range(-num+1, num +1):
        mat[base+num][base+x] = test(base+num, base+x, mat)
    for x in range(-num, num +1):
        mat[base-x][base+num] = test(base-x, base+num, mat)
    for x in range(-num, num +1):
        mat[base-num][base-x] = test(base-num, base-x, mat)
    for x in range(-num, num +1):
        mat[base+x][base-num] = test(base+x, base-num, mat)
    return mat


base = 5
mat = []
for x in range(0,11):
    row = []
    for y in range(0,11):
        row.append(0)
    mat.append(row)
mat[base][base] = 1
print mat[0]
print mat[1]
print mat[2]
print mat[3]
print mat[4]
print mat[5]
print mat[6]
print mat[7]
print mat[8]
print mat[9]
print mat[10]
print "---------------------------------------"
for x in range(1, 5):
    mat = add(base, x, mat)
print mat[0]
print mat[1]
print mat[2]
print mat[3]
print mat[4]
print mat[5]
print mat[6]
print mat[7]
print mat[8]
print mat[9]
print mat[10]

#
