import sys
sys.setrecursionlimit(10**6)
from collections import deque

# def dfs(y,x,visited,sl,h,w):
#     dxy=[[-1,0],[1,0],[0,-1],[0,1]]
#     for dx,dy in dxy:
#         yy=y+dy
#         xx=x+dx
#         if yy<0 or h<=yy or xx<0 or w<=xx:continue
#         typ=sl[yy][xx]
#         if visited[yy][xx]: continue
#         if typ=='#':continue
#         if typ=='^' and dy!=1:continue
#         if typ=='v' and dy!=-1:continue
#         if typ=='>' and dx!=-1:continue
#         if typ=='<' and dx!=1:continue
#         visited[yy][xx]=True
#         dfs(yy,xx,visited,sl,h,w)

h,w=map(int, input().split())
r,c=map(int, input().split())
r-=1
c-=1
sl=[]
for _ in range(h):
    row=list(input())
    sl.append(row)

visited=[[False]*w for _ in range(h)]
q=deque([(r,c)])
visited[r][c]=True
dxy=[[-1,0],[1,0],[0,-1],[0,1]]
while q:
    y,x=q.popleft()
    for dx,dy in dxy:
        yy=y+dy
        xx=x+dx
        if yy<0 or h<=yy or xx<0 or w<=xx:continue
        typ=sl[yy][xx]
        if visited[yy][xx]: continue
        if typ=='#':continue
        if typ=='^' and dy!=1:continue
        if typ=='v' and dy!=-1:continue
        if typ=='>' and dx!=-1:continue
        if typ=='<' and dx!=1:continue
        visited[yy][xx]=True
        q.append((yy,xx))

for i in range(h):
    row=visited[i]
    srow=sl[i]
    ansl=[]
    for j in range(w):
        if srow[j]=='#':ansl.append('#')
        elif row[j]:ansl.append('o')
        else:ansl.append('x')
    print(''.join(ansl))