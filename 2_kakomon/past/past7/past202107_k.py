import heapq
def dijkstra(s, n, g, al): # s: start, n: |V|, g; glaph (to,cost)
    INF = 10**18
    d = [INF] * n
    dv=[0]*n
    d[s] = 0
    dv[s]=al[s]
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heappush(que, (0, s))
    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for next_v, cost in g[v]:
            if d[next_v] > d[v] + cost:
                d[next_v] = d[v] + cost
                dv[next_v] = dv[v]+al[next_v]
                heapq.heappush(que, (d[next_v], next_v))
            elif d[next_v] == d[v] + cost:
                d[next_v] = d[v] + cost
                dv[next_v] = max(dv[v]+al[next_v], dv[next_v])
                # heapq.heappush(que, (d[next_v], next_v))
    return dv[n-1]


n,m=map(int, input().split())
al=list(map(int, input().split()))


g = [ [] for _ in range(n)]
for _ in range(m):
    u,v,t = map(int, input().split())
    u-=1
    v-=1
    g[u].append((v,t))
    g[v].append((u,t))

ans=dijkstra(0,n,g,al)
print(ans)