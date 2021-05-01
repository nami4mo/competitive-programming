print(pow(0.99,10000))
h,w=map(int, input().split())
cl=[]
sy,sx=-1,-1
gy,gx=-1,-1
for y in range(h):
    s=input()
    row=[]
    for x,si in enumerate(s):
        if si=='s':
            sy,sx=y,x
            row.append('s')
        elif si=='g':
            gy,gx=y,x
            row.append('g')
        elif si=='#':
            row.append('#')
        else:
            row.append(int(si))
    cl.append(row)

t99s=[1]
for i in range(1,h*w):
    t99s.append(t99s[-1]*0.99)

ok, ng = -1.0, 10.0
THRE=10**(-9)
from collections import deque
while abs(ok-ng) > THRE:
    mid = (ok+ng)/2
    res = False
    # ...
    q=deque()
    dists=[[-1]*w for _ in range(h)]
    dists[sy][sx]=0
    q.append((sy,sx))
    while q:
        py,px=q.popleft()
        pd=dists[py][px]
        # t99=pow(0.99,pd+1)
        t99=t99s[pd+1]
        for yy,xx in [(py+1,px),(py-1,px),(py,px+1),(py,px-1)]:
            if not (0<=yy<h and 0<=xx<w):continue
            if dists[yy][xx]!=-1:continue
            if cl[yy][xx]=='g':
                res=True
                break
            if cl[yy][xx]=='#':continue
            if cl[yy][xx]*t99<mid:continue
            dists[yy][xx]=pd+1
            q.append((yy,xx))
        if res:
            break

    if res: ok = mid
    else: ng = mid
if ok<0:ok=-1
print(ok)
