s = input()
n = len(s)
ind = n-1

eds = ['dream','dreamer','erase','eraser']

while True:
    for ed in eds:
        if ind+1 < len(ed): continue
        if s[ind+1-len(ed):ind+1] == ed:
            ind -= len(ed)
            break
    else:
        print('NO')
        exit()
    if ind < 0:
        break
print('YES')