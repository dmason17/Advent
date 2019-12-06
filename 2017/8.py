f = open('8.txt', 'r')
highestEver = 0
list = []
for line in f:
    lineSplit = line.split()
    list.append((lineSplit[0], 0))
f.close()

dict = dict(list)

f = open('8.txt', 'r')
for line in f:
    lineSplit = line.split()
    if lineSplit[5] == '>':
        if dict[lineSplit[4]] > int(lineSplit[6]):
            positive = 1
            if lineSplit[1] == 'dec':
                positive = -1
            dict[lineSplit[0]] += (positive * int(lineSplit[2]))
            if dict[lineSplit[0]] > highestEver:
                highestEver = dict[lineSplit[0]]
    if lineSplit[5] == '<':
        if dict[lineSplit[4]] < int(lineSplit[6]):
            positive = 1
            if lineSplit[1] == 'dec':
                positive = -1
            dict[lineSplit[0]] += (positive * int(lineSplit[2]))
            if dict[lineSplit[0]] > highestEver:
                highestEver = dict[lineSplit[0]]
    if lineSplit[5] == '>=':
        if dict[lineSplit[4]] >= int(lineSplit[6]):
            positive = 1
            if lineSplit[1] == 'dec':
                positive = -1
            dict[lineSplit[0]] += (positive * int(lineSplit[2]))
            if dict[lineSplit[0]] > highestEver:
                highestEver = dict[lineSplit[0]]
    if lineSplit[5] == '<=':
        if dict[lineSplit[4]] <= int(lineSplit[6]):
            positive = 1
            if lineSplit[1] == 'dec':
                positive = -1
            dict[lineSplit[0]] += (positive * int(lineSplit[2]))
            if dict[lineSplit[0]] > highestEver:
                highestEver = dict[lineSplit[0]]
    if lineSplit[5] == '==':
        if dict[lineSplit[4]] == int(lineSplit[6]):
            positive = 1
            if lineSplit[1] == 'dec':
                positive = -1
            dict[lineSplit[0]] += (positive * int(lineSplit[2]))
            if dict[lineSplit[0]] > highestEver:
                highestEver = dict[lineSplit[0]]
    if lineSplit[5] == '!=':
        if dict[lineSplit[4]] != int(lineSplit[6]):
            positive = 1
            if lineSplit[1] == 'dec':
                positive = -1
            dict[lineSplit[0]] += (positive * int(lineSplit[2]))
            if dict[lineSplit[0]] > highestEver:
                highestEver = dict[lineSplit[0]]
f.close()

highestNum = 0
for a, b in dict.items():
    if b > highestNum:
        highestNum = b
print highestNum
print highestEver
