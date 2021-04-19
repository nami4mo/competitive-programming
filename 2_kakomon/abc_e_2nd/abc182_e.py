import sys
input = sys.stdin.readline

h,w,n,m=map(int, input().split())
sl=[[0]*w for _ in range(h)]
for _ in range(n):
    a,b=map(int, input().split())
    a-=1
    b-=1
    sl[a][b]=1

for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    sl[a][b]=-1

# print(sl)
light=[[False]*w for _ in range(h)]
ssl=[[0]*h for _ in range(w)]
for y in range(h):
    ok1=False
    ok2=False
    for x in range(w):
        v=sl[y][x]
        if v==-1:ok1=False
        elif v==1:ok1=True
        if ok1:light[y][x]=True
        x2=w-1-x
        v2=sl[y][x2]
        if v2==-1:ok2=False
        elif v2==1:ok2=True
        if ok2:light[y][x2]=True
        ssl[x][y]=v

for x in range(w):
    ok1=False
    ok2=False
    for y in range(h):
        v=ssl[x][y]
        if v==-1:ok1=False
        elif v==1:ok1=True
        if ok1:light[y][x]=True
        y2=h-1-y
        v2=ssl[x][y2]
        if v2==-1:ok2=False
        elif v2==1:ok2=True
        if ok2:light[y2][x]=True

ans=0
for y in range(h):
    for x in range(w):
        if light[y][x]:ans+=1
print(ans)