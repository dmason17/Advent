import time

input = [
(1, 1),
(1, 6),
(8, 3),
(3, 4),
(5, 5),
(8, 9)]

input = [
(181, 184),
(230, 153),
(215, 179),
(84, 274),
(294, 274),
(127, 259),
(207, 296),
(76, 54),
(187, 53),
(318, 307),
(213, 101),
(111, 71),
(310, 295),
(40, 140),
(176, 265),
(98, 261),
(315, 234),
(106, 57),
(40, 188),
(132, 292),
(132, 312),
(97, 334),
(292, 293),
(124, 65),
(224, 322),
(257, 162),
(266, 261),
(116, 122),
(80, 319),
(271, 326),
(278, 231),
(191, 115),
(277, 184),
(329, 351),
(58, 155),
(193, 147),
(45, 68),
(310, 237),
(171, 132),
(234, 152),
(158, 189),
(212, 100),
(346, 225),
(257, 159),
(330, 112),
(204, 320),
(199, 348),
(207, 189),
(130, 289),
(264, 223)
]

alphS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphL = list(alphS)
alphL.append('AA')
alphL.append('BB')
alphL.append('CC')
alphL.append('DD')
alphL.append('EE')
alphL.append('FF')
alphL.append('GG')
alphL.append('HH')
alphL.append('II')
alphL.append('JJ')
alphL.append('KK')
alphL.append('LL')
alphL.append('MM')
alphL.append('NN')
alphL.append('OO')
alphL.append('PP')
alphL.append('QQ')
alphL.append('RR')
alphL.append('SS')
alphL.append('TT')
alphL.append('UU')
alphL.append('VV')
alphL.append('WW')
alphL.append('XX')
alphL.append('YY')
alphL.append('ZZ')
alphL.append('AAA')
alphL.append('BBB')

highx = 0
highy = 0
for x in input:
    if x[0] > highy:
        highy = x[0]
    if x[1] > highx:
        highx = x[1]

print highx
print highy
print "Building list"

grid = []
for x in range(0, highx+1):
    row = []
    for y in range(0, highy+1):
        row.append('.')
    grid.append(row)

for x in range(0, len(input)):
    grid[input[x][1]][input[x][0]] =alphL[x]

print "Assigning letters"

for y in range(0, highy+1):
    for x in range(0, highx+1):
        if grid[x][y] not in alphL:
            maxDiff = 1000
            letter = ''
            for z in input:
                if grid[z[1]][z[0]] in alphL and (abs(z[0] - y) + abs(z[1] - x)) < maxDiff:
                    maxDiff = (abs(z[0] - y) + abs(z[1] - x))
                    letter = grid[z[1]][z[0]].lower()
                elif grid[z[1]][z[0]] in alphL and (abs(z[0] - y) + abs(z[1] - x)) == maxDiff:
                    letter = '.'
            grid[x][y] = letter


print "Finding maximums"
minx = 10000
maxx = 0
miny = 10000
maxy = 0
for x in input:
    if x[0] < minx:
        minx = x[0]
    if x[0] > maxx:
        maxx = x[0]
    if x[1] < miny:
        miny = x[1]
    if x[1] > maxy:
        maxy = x[1]

print minx
print maxx
print miny
print maxy

print "Checking..."
lettersToCheck = []
for x in range(minx+1, maxx-1):
    for y in range(miny+1, maxy-1):
        if grid[y][x] in alphL:
            lettersToCheck.append(grid[y][x])


print lettersToCheck
print "-----------"
for x in grid:
    for y in x:
        print y ,
    print ''

for z in lettersToCheck:
    count = 0
    for y in range(0, highy+1):
        for x in range(0, highx+1):
            if grid[x][y].lower() == z.lower():
                count += 1
    print z + " " + str(count)
