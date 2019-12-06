ids = 0
f = open('4.txt', 'r')
for line in f:
    lineSplit = line.split("-")
    word = ""
    all_freq ={}
    letterList = []
    for x in range(0, len(lineSplit)-1):
        word = word + lineSplit[x]
    for i in word:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    sol = []
    for y in range(0, 20):
        for x in sorted(all_freq):
            if all_freq[x] == 20-y and len(sol) < 5:
                sol.append(x)

    answer = ''
    for x in sol:
        answer = answer + x

    if answer == lineSplit[len(lineSplit)-1][len(lineSplit[len(lineSplit)-1])-7:len(lineSplit[len(lineSplit)-1])-2]:
        newId = int(lineSplit[len(lineSplit)-1].split("[")[0])
        ids = ids + newId
        wordList = list(word)
        newWord = ''
        for x in wordList:
            if ord(x) != 45:
                newWord = newWord + chr(((ord(x.lower())-97+newId) % 26 ) + 97)
        if newWord == 'northpoleobjectstorage':
            print newId

print ids
