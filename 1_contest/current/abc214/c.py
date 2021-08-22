n=int(input())
sl=list(map(int, input().split()))
tl=list(map(int, input().split()))

import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph (to,cost)
    INF = 10**18
    d = [INF] * n
    #-- record the prev vertex of each one for restoring the route --
    # prev_vl = [-1]*n 
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                # prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))

    return d

gl=[[] for _ in range(n+1)]
for i in range(n):
    gl[n].append((i,tl[i]))

for i in range(n-1):
    gl[i].append((i+1,sl[i]))
gl[n-1].append((0,sl[n-1]))

ans = dijkstra(n, n+1, gl)
for i in range(n):
    print(ans[i])