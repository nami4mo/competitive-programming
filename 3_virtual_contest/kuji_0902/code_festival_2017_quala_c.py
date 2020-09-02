h,w = map(int, input().split())
al = [list(input()) for _ in range(h)]
cnts = {}
for row in al:
    for a in row:
        cnts.setdefault(a,0)
        cnts[a] += 1
        cnts[a]%= 4

c4 = [0]*5
for i,v in cnts.items():
    c4[v] += 1
c4[4] = c4[0]


if w%2 == 0 and h%2 == 0:
    if c4[1] == 0 and c4[2] == 0 and c4[3] == 0:
        print('Yes')
    else:
        print('No')

elif w%2 == 1 and h%2 == 1:
    if c4[1] + c4[3] == 1 and c4[3] + c4[2] <= (h-1)//2 + (w-1)//2:
        print('Yes')
    else:
        print('No')

elif w%2 == 1 and h%2 == 0:
    if c4[1] + c4[3] == 0 and c4[2] <= h//2:
        print('Yes')
    else:
        print('No')

elif w%2 == 0 and h%2 == 1:
    if c4[1] + c4[3] == 0 and c4[2] <= w//2:
        print('Yes')
    else:
        print('No')