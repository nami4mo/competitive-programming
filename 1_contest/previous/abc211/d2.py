import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph (to,cost)
    INF = 10**18
    d = [INF] * n
    dcnt = [0] * n

    #-- record the prev vertex of each one for restoring the route --
    # prev_vl = [-1]*n 
    d[s] = 0
    dcnt[s] = 1
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))
    used=[False]*n
    while que:
        dist, v = heapq.heappop(que)
        if v==n-1:break
        if used[v]:continue
        if d[v] < dist: continue # if v has been already used -> continue
        used[v]=True
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                # prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))
                dcnt[next_v]=dcnt[v]
            elif d[next_v] == d[v] + cost:
                dcnt[next_v]+=dcnt[v]
    return dcnt[n-1]

n,m = map(int, input().split())
g = [ [] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
# ans = dijkstra(0, n, g)
# print(ans)

INF = 10**18

d=[INF]*n
dcnt=[0]*n
d[0]=0
dcnt[0]=1

MOD=10**9+7
from collections import deque
q=deque([0])
while q:
    poped=q.popleft()
    for neib in g[poped]:
        if d[neib]>=INF:
            d[neib]=d[poped]+1
            dcnt[neib]+=dcnt[poped]
            q.append(neib)
        elif d[neib]==d[poped]+1:
            dcnt[neib]+=dcnt[poped]
print(dcnt[n-1]%MOD)
