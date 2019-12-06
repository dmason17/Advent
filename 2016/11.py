def createFloor(num):
    newScreen = []
    for x in range(0, 4):
        row = []
        for y in range (0, 1 + num):
            if y == 0:
                row.append('F'+str(x+1))
            row.append('..')
        newScreen.append(row)
    return newScreen

def enrichFloor(floor):
    floor[0][1] = 'E '
    floor[0][2] = 'PG'
    floor[0][3] = 'TG'
    floor[0][4] = 'TM'
    floor[0][5] = 'PRG'
    floor[0][6] = 'RG'
    floor[0][7] = 'RM'
    floor[0][8] = 'CG'
    floor[0][9] = 'CM'

    floor[1][10] = 'PM'
    floor[1][11] = 'PRM'
    return floor

floor = createFloor(10)
floor = enrichFloor(floor)
for x in floor:
    print x
