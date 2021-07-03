import heapq
from math import sqrt
INF = 10**18

def dijkstra(s, n, g): # s: start, n: |V|, g; glaph (to,cost)
    d = [INF] * n
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost, di in g[v]:
            t = dist # d[v]
            t1 = int(sqrt(di))-1
            t2 = int(sqrt(di))
            if t>=t2:
                c = cost+di//(t+1)
            else:
                c1= (t1-t)+cost+di//(t1+1)
                c2= (t2-t)+cost+di//(t2+1)
                c3= cost+di//(t+1)
                c=min(c1,c2,c3)
            if d[next_v] > d[v] + c:
                d[next_v] = d[v] + c
                heapq.heappush(que, (d[next_v], next_v))
    return d


n,m=map(int, input().split())
gl=[[] for _ in range(n)]
for _ in range(m):
    a,b,c,d=map(int, input().split())
    a-=1
    b-=1
    gl[a].append((b,c,d))
    gl[b].append((a,c,d))

d=dijkstra(0,n,gl)
ans=d[n-1]
if ans>=INF:print(-1)
else:print(ans)