h,w=map(int, input().split())
sl=[]
sl.append(['#']*(w+2))
for _ in range(h):
    row=['#']+list(input())+['#']
    sl.append(row)
sl.append(['#']*(w+2))

tl=[]
dx=[-1,0,1]
dy=[-1,0,1]
for i in range(1,h+1):
    row=[]
    for j in range(1,w+1):
        ok=True
        for dxx in dx:
            for dyy in dy:
                if sl[i+dyy][j+dxx]=='.':ok=False
        if ok: row.append('#')
        else: row.append('.')
    tl.append(row)

ssl=[['.']*(w+2) for _ in range(h+2)]
for i in range(0,h):
    row=[]
    for j in range(0,w):
        if tl[i][j]=='.':continue
        for dxx in dx:
            for dyy in dy:
                ssl[i+dyy+1][j+dxx+1]='#'

for i in range(1,h+1):
    for j in range(1,w+1):
        if sl[i][j]!=ssl[i][j]:
            print('impossible')
            exit()

print('possible')
for row in tl:
    print(''.join(row))