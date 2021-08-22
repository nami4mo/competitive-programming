h,w,k=map(int, input().split())
y1,x1,y2,x2=map(int, input().split())
y1-=1
x1-=1
y2-=1
x2-=1
cl=[]
for _ in range(h):
    row=list(input())
    cl.append(row)

from collections import deque
INF=10**8
ds=[[INF]*w for _ in range(h)]
visited=[[False]*w for _ in range(h)]
ds[y1][x1]=0
q=deque([(y1,x1)])
while q:
    cy,cx=q.popleft()
    if visited[cy][cx]:continue
    # print(cy,cx)
    visited[cy][cx]=True
    cd=ds[cy][cx]
    for dx in range(1,k+1):
        xx=cx+dx
        # print(cy,xx)
        if xx>=w or ds[cy][xx]<=cd or cl[cy][xx]=='@':break
        ds[cy][xx]=cd+1
        q.append((cy,xx))
    for dx in range(1,k+1):
        xx=cx+dx*(-1)
        # print(cy,xx)
        if xx<0 or ds[cy][xx]<=cd or cl[cy][xx]=='@':break
        ds[cy][xx]=cd+1
        q.append((cy,xx))
    for dy in range(1,k+1):
        yy=cy+dy
        if yy>=h or ds[yy][cx]<=cd or cl[yy][cx]=='@':break
        ds[yy][cx]=cd+1
        q.append((yy,cx))
    for dy in range(1,k+1):
        yy=cy+dy*(-1)
        if yy<0 or ds[yy][cx]<=cd or cl[yy][cx]=='@':break
        ds[yy][cx]=cd+1
        q.append((yy,cx))
    if cy==y2 and cx==x2:break

if ds[y2][x2]==INF:print(-1)
else:print(ds[y2][x2])
# for row in ds:print(*row)