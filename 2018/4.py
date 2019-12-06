import time

start = time.time()

lineList = []
f = open('4.txt', 'r')
for line in f:
    lineList.append(line)

orderedList = []
for month in range(1, 13):
    for day in range(1, 32):
        for hour in range(0, 24):
            for minute in range(0, 60):
                for x in lineList:
                    if int(x.split()[0].split('-')[1]) == month and int(x.split()[0].split('-')[2]) == day and int(x.split()[1][:2]) == hour and int(x.split()[1][3:5]) == minute:
                        orderedList.append(x)

print 'Date\tID\tMinute'
print '\t\t000000000011111111112222222222333333333344444444445555555555'
print '\t\t012345678901234567890123456789012345678901234567890123456789'

newGuard = False
id = ''
timeline = '............................................................'
timelineList = list(timeline)
date = ''
masterList = []
found = False
for x in orderedList:
    if x.split()[2] == 'Guard':
        if newGuard:
            found = False
            for z in masterList:
                if z[0] == id:
                    found = True
                    z[1].append(timelineList)
            if not found:
                timeList = list([timelineList])
                idList = list([id, timeList])
                masterList.append(idList)
            print date + '\t' + id + '\t' + ''.join(timelineList)
        id = str(x.split()[3])
        date = str(x.split()[0][6:11])
        timeline = '............................................................'
        timelineList = list(timeline)
        newGuard = True
    elif x.split()[2] == 'falls':
        asleepIndex = int(x.split()[1][3:5])
    elif x.split()[2] == 'wakes':
        wakeIndex = int(x.split()[1][3:5])
        for y in range(asleepIndex, wakeIndex):
            timelineList[y] = '#'
# last loop / print
for z in masterList:
    if z[0] == id:
        found = True
        z[1].append(timelineList)
if not found:
    timeList = list([timelineList])
    idList = list([id, timeList])
    masterList.append(idList)
print date + '\t' + id + '\t' + ''.join(timelineList)

longestSleep = 0
winner = ''
for x in masterList:
    count = 0
    for y in x[1]:
        for z in y:
            if z == '#':
                count += 1
    if count > longestSleep:
        longestSleep = count
        winner = x[0]


count = 0
minute = 0
for x in masterList:
    if x[0] == winner:
        for min in range(0,60):
            minCount = 0
            for y in x[1]:
                if y[min] == '#':
                    minCount += 1
            if minCount > count:
                count = minCount
                minute = min

otherCount = 0
otherMinute = 0
otherWinner = ''
for x in masterList:
        for min in range(0,60):
            minCount = 0
            for y in x[1]:
                if y[min] == '#':
                    minCount += 1
            if minCount > otherCount:
                otherCount = minCount
                otherMinute = min
                otherWinner = x[0]


end = time.time()
print '---------------------'
print 'winner 1: ' + winner
print 'minute 1: ' + str(minute)
print 'answer 1: ' + str(int(winner[1:]) * minute)

print 'winner 2: ' + otherWinner
print 'minute 2: ' + str(otherMinute)
print 'answer 2: ' + str(int(otherWinner[1:]) * otherMinute)
print 'finished in ' + str(end-start) + 's'

#
# [
#     [10, [qwe, ytr, ytre]],
#     [11, [qwe]]
# ]
