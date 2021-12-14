s = input()
l = 0
if s == '{}':
    print('dict')
    exit()
for si in s:
    if si == '{':
        l += 1
    elif si == '}':
        l -= 1

    if l == 1:
        if si == ':':
            print('dict')
            break
        elif si == ',':
            print('set')
            break
else:
    print('set')
