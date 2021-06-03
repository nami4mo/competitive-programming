h,w=map(int, input().split())
rs,cs=map(int, input().split())
rt,ct=map(int, input().split())
rs-=1;cs-=1;rt-=1;ct-=1

sl=[list(input()) for _ in range(h)]

dist=[[10**10]*w for _ in range(h)]
from collections import deque
q=deque()
q.append((rs,cs))
dist[rs][cs]=0
end=False
while q:
    py,px=q.popleft()
    # print(py,px)
    d=dist[py][px]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for dy,dx in dirs:
        for i in range(1,10**3+1):
            yy=py+dy*i
            xx=px+dx*i
            if not (0<=yy<h and 0<=xx<w):break
            if sl[yy][xx]=='#':break
            if dist[yy][xx]<=d:break
            dist[yy][xx]=min(d+1,dist[yy][xx])
            q.append((yy,xx))
            if yy==rt and xx==ct:
                end=True
                print(dist[yy][xx]-1)
                exit()