from typing import Coroutine


s = (input())

if len(s) == 1:
    if s == '8': print('Yes')
    else: print('No')
    exit()

if len(s) == 2:
    v = int(s)
    v2 = int(s[::-1])
    if v%8 == 0 or v2%8 == 0: print('Yes')
    else: print('No')
    exit()

cnts = [0]*10
for i in range(1,10):
    cnts[i] = s.count(str(i))


for i in range(1000):
    v = i*8
    if v <= 100: continue
    sv = str(v)
    if '0' in sv: continue
    sv = sv[-3:]
    for j in range(1,10):
        if cnts[j] < sv.count(str(j)):
            break
    else:
        print('Yes')
        exit()

print('No')