from collections import deque
def check(al):
    for y in range(10):
        for x in range(10):
            if al[y][x]=='o':
                sy,sx=y,x

    q=deque()
    q.append((sy,sx))
    c=1
    vis=[[False]*10 for _ in range(10)]
    vis[sy][sx]=True
    while q:
        y,x=q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            yy,xx=y+dy,x+dx
            if not (0<=yy<10 and 0<=xx<10):continue
            if not vis[yy][xx] and al[yy][xx]=='o':
                c+=1
                vis[yy][xx]=True
                q.append((yy,xx))
    return c
    

al=[list(input()) for _ in range(10)]
cnt=0
for y in range(10):
    for x in range(10):
        if al[y][x]=='o':cnt+=1

for y in range(10):
    for x in range(10):
        if al[y][x]=='o':continue
        al[y][x]='o'
        if cnt+1==check(al):
            print('YES')
            exit()
        al[y][x]='x'
print('NO')