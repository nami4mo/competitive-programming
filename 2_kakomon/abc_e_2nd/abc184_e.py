h,w=map(int, input().split())
sl=[list(input()) for _ in range(h)]

start=(-1,-1)
goal=(-1,-1)
cl={chr(ord('a')+i):[] for i in range(26)}

for i in range(h):
    for j in range(w):
        v=sl[i][j]
        if v=='#':continue
        if v=='S':start=(i,j)
        elif v=='G':goal=(i,j)
        elif v=='.':pass
        else:
            cl[v].append((i,j))

from collections import deque
q=deque()
q.append(start)
dists=[[-1]*w for _ in range(h)]
dists[start[0]][start[1]]=0
used={chr(ord('a')+i):False for i in range(26)}

while q:
    y,x=q.popleft()
    d=dists[y][x]
    if (y,x)==goal:
        print(d)
        exit()
    for yy,xx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
        if not (0<=yy<h and 0<=xx<w):continue
        if dists[yy][xx]!=-1:continue
        if sl[yy][xx]=='#':continue
        dists[yy][xx]=d+1
        q.append((yy,xx))
    if ord('a')<=ord(sl[y][x])<=ord('z'):
        c=sl[y][x]
        if used[c]:continue
        for yy,xx in cl[c]:
            if dists[yy][xx]!=-1:continue
            dists[yy][xx]=d+1
            q.append((yy,xx))
        used[c]=True
print(-1)