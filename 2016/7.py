count = 0
f = open('7.txt', 'r')
for line in f:
    success = False
    wordList = []
    badWordList = []
    lineSplit = line.split("]")
    for x in lineSplit:
        wordList.append(x.split("[")[0])
        if len(x.split("[")) > 1:
            badWordList.append(x.split("[")[1])
    cont = True
    for x in badWordList:
        if len(x) > 3:
            charSplit = list(x)
            for y in range (0, len(x)-3):
                if charSplit[y] != charSplit[y+1] and charSplit[y] == charSplit[y+3] and charSplit[y+1] == charSplit[y+2]:
                    cont = False

    if cont:
        for x in wordList:
            if len(x) > 3:
                charSplit = list(x)
                for y in range (0, len(x)-3):
                    if charSplit[y] != charSplit[y+1] and charSplit[y] == charSplit[y+3] and charSplit[y+1] == charSplit[y+2]:
                        success = True

    if success:
        count = count + 1

print count


count = 0
f = open('7.txt', 'r')
for line in f:
    success = False
    wordList = []
    badWordList = []
    lineSplit = line.split("]")
    for x in lineSplit:
        wordList.append(x.split("[")[0])
        if len(x.split("[")) > 1:
            badWordList.append(x.split("[")[1])

    possibleMatches = []
    for x in badWordList:
        if len(x) > 2:
            charSplit = list(x)
            for y in range (0, len(x)-2):
                if charSplit[y] != charSplit[y+1] and charSplit[y] == charSplit[y+2]:
                    possibleMatches.append(charSplit[y+1]+charSplit[y]+charSplit[y+1])

    for x in wordList:
        if len(x) > 2:
            charSplit = list(x)
            for y in range (0, len(x)-2):
                if charSplit[y] != charSplit[y+1] and charSplit[y] == charSplit[y+2]:
                    for z in possibleMatches:
                        if charSplit[y] + charSplit[y+1] + charSplit[y+2] == z:
                            success = True

    if success:
        count = count + 1

print count
