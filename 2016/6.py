doubleArray = [[], [], [], [], [], [], [], [], []]

f = open('6.txt', 'r')
for line in f:
    wordList = list(line)
    for x in range(0, len(wordList)):
        doubleArray[x].append(wordList[x])

for x in range(0, len(doubleArray)):
    all_freq = {}
    for i in doubleArray[x]:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    #count = 0
    count = 1000
    letter = ''
    for y in all_freq:
        #if all_freq[y] > count:
        if all_freq[y] < count:
            count = all_freq[y]
            letter = y
    print letter
