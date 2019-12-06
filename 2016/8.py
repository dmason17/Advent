def createScreen():
    newScreen = []
    for x in range(0, 6):
        row = []
        for y in range (0, 50):
            row.append('.')
        newScreen.append(row)
    return newScreen

def printScreen(inputScreen):
    for x in range(0, len(inputScreen)):
        print inputScreen[x]

def rotate(list, num):
    output_list = []
    for item in range(len(list) - num, len(list)):
        output_list.append(list[item])
    for item in range(0, len(list) - num):
        output_list.append(list[item])
    return output_list

def countScreen(inputScreen):
    count = 0
    for x in range(0, len(inputScreen)):
        for y in range(0, len(inputScreen[x])):
            if inputScreen[x][y] == '#':
                count = count + 1
    return count

screen = createScreen()
f = open('8.txt', 'r')
for line in f:
    commands = line.split()
    if commands[0] == 'rect':
        for x in range(0, int(commands[1].split('x')[1])):
            for y in range(0, int(commands[1].split('x')[0])):
                screen[x][y] = '#'
    elif commands[0] == 'rotate':
        if commands[1] == 'column':
            listToRotate = []
            for x in range (0, 6):
                listToRotate.append(screen[x][int(commands[2].split('=')[1])])
            listToRotate = rotate(listToRotate, int(commands[4]))
            for x in range(0, 6):
                screen[x][int(commands[2].split('=')[1])] = listToRotate[x]
        if commands[1] == 'row':
            screen[int(commands[2].split('=')[1])] = rotate(screen[int(commands[2].split('=')[1])], int(commands[4]))


printScreen(screen)
print countScreen(screen)
