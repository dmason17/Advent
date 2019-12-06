import hashlib

def isInt(x):
    try:
        int(x)
        return True
    except:
        return False

input = 'ugkcyxxp'
x = 0
y = 0
answer = ''
secondAnswer = [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ']
while y < 15:
    word = input + str(x)
    if hashlib.md5(word.encode()).hexdigest()[0:5] == '00000':
        if len(answer) < 8:
            answer = answer +  str(hashlib.md5(word.encode()).hexdigest()[5:6])
        if isInt(hashlib.md5(word.encode()).hexdigest()[5:6]) and int(hashlib.md5(word.encode()).hexdigest()[5:6]) < 8:
            secondAnswer[int(hashlib.md5(word.encode()).hexdigest()[5:6])] = hashlib.md5(word.encode()).hexdigest()[6:7]
            print secondAnswer
            y = y + 1
    x = x + 1

print answer
