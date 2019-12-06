lineList = []
newLineList = []
stepList = []
preReqList = []
answer = ''
answerList = []

f = open('7.txt', 'r')
for line in f:
    lineList.append(line)
    stepList.append(line.split()[1])
    preReqList.append(line.split()[7])
f.close()

uniqueSteps = set(stepList)
uniquePreReq = set(preReqList)
topElement = list(uniqueSteps - uniquePreReq)
topElement = sorted(topElement)
answer = topElement[0]
answerList.append(topElement[0])
max = len(uniqueSteps)
######################################################
while max != len(answerList):
    newLineList = []
    stepList = []
    preReqList = []
    for x in lineList:
        if x.split()[1] != answer:
            newLineList.append(x)
            stepList.append(x.split()[1])
            preReqList.append(x.split()[7])

    lineList = newLineList
    uniqueSteps = set(stepList)
    uniquePreReq = set(preReqList)
    topElement = list(uniqueSteps - uniquePreReq)
    topElement = sorted(topElement)
    answer = topElement[0]
    answerList.append(topElement[0])
######################################################

for x in uniquePreReq:
    answerList.append(x)
print ('').join(answerList
