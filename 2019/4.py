# for part 1
def doubleCheck(num):
    if len(num) == len(set(num)):
        return False
    else:
        curr = 10
        for x in num:
            if x == curr:
                return True
            else:
                curr = x
        return False

# for part 2
def onlyTwoCheck(num):
    if len(num) == len(set(num)):
        return False
    else:
        curr = 10
        for x in set(num):
            if num.count(x) == 2:
                print str(num)
                return True
        print str(num) + 'X'
        return False

def nextNum(num):
    count = 1
    cont = True
    while cont or count > len(num):
        if num[len(num)-count] == 9:
            count += 1
        else:
            num[len(num)-count] += 1
            for x in range(1, count):
                num[len(num)-x] = num[len(num)-count]
            cont = not doubleCheck(num)
    return num

low = [2, 3, 5, 7, 7 ,6]
high = [7, 0, 6, 9, 4, 8]

count = 0
while int(''.join(map(str,low))) < int(''.join(map(str,high))):
    if onlyTwoCheck(nextNum(low)):
        count += 1

print count - 1
