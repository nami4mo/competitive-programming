import heapq
from math import sqrt
def dijkstra(s, n, xytrl): # s: start, n: |V|, g; glaph (to,cost)
    INF = 10**8
    d = [INF] * n
    #-- record the prev vertex of each one for restoring the route --
    # prev_vl = [-1]*n 
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        x,y,t,r=xytrl[v]
        for next_v in range(n):
            xx,yy,tt,rr=xytrl[next_v]
            cost=sqrt( ((x-xx)**2+(y-yy)**2)/(min(t,rr)**2) )
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                heapq.heappush(que, (d[next_v], next_v))
    return d

n=int(input())
xytrl=[]
for _ in range(n):
    x,y,t,r=map(int, input().split())
    xytrl.append((x,y,t,r))

# gl=[[] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i==j:continue
#         xx,yy,tt,rr=xytrl[j]
#         d=((x-xx)**2+(y-yy)**2)**0.5
#         cost=d/min(t,rr)
#         gl[i].append((j,cost))

d=dijkstra(0,n,xytrl)[1:]
d.sort(reverse=True)
ans=0
for i in range(n-1):
    d[i]+=i
    ans=max(ans,d[i])
print(ans)