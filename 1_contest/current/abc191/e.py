from heapq import heappop, heappush, heapify
import heapq

def dijkstra(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    d = [INF] * n
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                heapq.heappush(que, (d[next_v], next_v))
    return d


n,m=map(int, input().split())
abcl=[]
for _ in range(m):
    a,b,c=map(int, input().split())
    a-=1
    b-=1
    abcl.append((a,b,c))

INF = 10**18
ansl=[]
for i in range(n):
    gl= [ [] for _ in range(n+1)]
    for a,b,c in abcl:
        if b==i:
            gl[a].append((n,c))
        else:
            gl[a].append((b,c))
    ds=dijkstra(i,n+1,gl)
    ans=ds[n]
    if ans>=INF: ans=-1
    ansl.append(ans)

for a in ansl:print(a)