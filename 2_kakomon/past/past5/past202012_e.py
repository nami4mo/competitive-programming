import numpy as np

def check(sl,tll):
    h=len(sl)
    w=len(sl[0])
    th=len(tll)
    tw=len(tll[0])
    for y in range(h-th+1):
        for x in range(w-tw+1):
            res=True
            for i in range(th):
                for j in range(tw):
                    if tll[i][j]=='#' and sl[y+i][x+j]=='#':
                        res=False
            if res: return True
    return False


h,w=map(int, input().split())
sl=[]
for _ in range(h):
    row=list(input())
    sl.append(row)

tl=[]
first_row=-1
last_row=-1
for i in range(h):
    row=list(input())
    tl.append(row)
    if '#' in row:
        if first_row==-1: first_row=i
        last_row=i

tl=tl[first_row:last_row+1]

first_x=-1
last_x=-1
for x in range(w):
    exist=False
    for y in range(len(tl)):
        if tl[y][x]=='#':
            break
    else:
        continue
    if first_x==-1: first_x=x
    last_x=x

tll=[]
for row in tl:
    tll.append(row[first_x:last_x+1])

ans1=check(sl,tll)
if ans1:
    print('Yes')
    exit()
for i in range(3):
    sl=np.array(sl)
    sl=np.rot90(sl)
    sl=sl.tolist()
    ans1=check(sl,tll)
    if ans1:
        print('Yes')
        exit()
print('No')