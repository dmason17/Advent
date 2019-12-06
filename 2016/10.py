instructions = []
bots = {}
outputs = {}
f = open('10.txt', 'r')
for line in f:
    if 'value' in line:
        if str(line.split()[5]) in bots:
            bots[line.split()[5]].append(int(line.split()[1]))
        else:
            bots[line.split()[5]] = [int(line.split()[1])]
    else:
        instructions.append(line)


def doWork(botNumber, botz, outputz):
    for x in instructions:
        if x.split()[1] == botNumber and x.split()[1] in botz:
            if 61 in botz[x.split()[1]] and 17 in botz[x.split()[1]]:
                print x.split()[1]
            #Decides which is high or low
            if botz[x.split()[1]][0] < botz[x.split()[1]][1]:
                #bots
                if x.split()[5] == 'bot' and x.split()[6] in botz:
                    botz[x.split()[6]].append(botz[x.split()[1]][0])
                elif x.split()[5] == 'bot':
                    botz[x.split()[6]] = [botz[x.split()[1]][0]]
                if x.split()[10] == 'bot' and x.split()[11] in botz:
                    botz[x.split()[11]].append(botz[x.split()[1]][1])
                elif x.split()[10] == 'bot':
                    botz[x.split()[11]] = [botz[x.split()[1]][1]]
                #Outputs
                if x.split()[5] == 'output' and x.split()[6] in outputz:
                    outputz[x.split()[6]].append(botz[x.split()[1]][0])
                elif x.split()[5] == 'output':
                    outputz[x.split()[6]] = [botz[x.split()[1]][0]]
                if x.split()[10] == 'output' and x.split()[11] in outputz:
                    outputz[x.split()[11]].append(botz[x.split()[1]][1])
                elif x.split()[10] == 'output':
                    outputz[x.split()[11]] = [botz[x.split()[1]][1]]
            else:
                #bots
                if x.split()[5] == 'bot' and x.split()[6] in botz:
                    botz[x.split()[6]].append(botz[x.split()[1]][1])
                elif x.split()[5] == 'bot':
                    botz[x.split()[6]] = [botz[x.split()[1]][1]]
                if x.split()[10] == 'bot' and x.split()[11] in botz:
                    botz[x.split()[11]].append(botz[x.split()[1]][0])
                elif x.split()[10] == 'bot':
                    botz[x.split()[11]] = [botz[x.split()[1]][0]]
                #Outputs
                if x.split()[5] == 'output' and x.split()[6] in outputz:
                    outputz[x.split()[6]].append(botz[x.split()[1]][1])
                elif x.split()[5] == 'output':
                    outputz[x.split()[6]] = [botz[x.split()[1]][1]]
                if x.split()[10] == 'output' and x.split()[11] in outputz:
                    outputz[x.split()[11]].append(botz[x.split()[1]][0])
                elif x.split()[10] == 'output':
                    outputz[x.split()[11]] = [botz[x.split()[1]][0]]
            bots[x.split()[1]] = []


workNeedsToBeDone = True
while workNeedsToBeDone:
    search = ''
    workNeedsToBeDone = False
    for x in bots:
        if len(bots[x]) == 2:
            search = x
            workNeedsToBeDone = True
            break
    if search != '':
        doWork(x, bots, outputs)


print outputs['0'][0] * outputs['1'][0] * outputs['2'][0]
