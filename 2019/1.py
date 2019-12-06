def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def calcFuel(mass):
    return truncate(mass / 3) - 2


total = 0
lineList = []
f = open('1.txt', 'r')
for line in f:
    lineList.append(line)

for line in lineList:
    mass = int(line)
    while mass > 0:
        mass = calcFuel(mass)
        if mass > 0:
            total = total + mass

print str(total)
