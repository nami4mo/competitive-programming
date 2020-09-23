import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    prev_vl = [-1]*n # record the prev vertex of each one for restoring the route
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
                prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))
    
    # resotre the route
    # route = [g]
    # curr_v = g
    # while True:
    #     prev_v = prev_vl[curr_v]
    #     if prev_v == -1: break
    #     else: route.append(prev_v)
    # route = route[::-1]
    # return d, route

    used_edges = []
    for i in range(n):
        if i == s: continue
        used_edges.append((prev_vl[i],i))
    return d, used_edges


n,m = map(int, input().split())
g = [ [] for _ in range(n)]
edges = [ [False]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().split())
    a-=1
    b-=1
    g[a].append((b,c))
    g[b].append((a,c))
    edges[a][b] = True
    edges[b][a] = True

for i in range(n):
    d, used_edges = dijkstra(i, n, g)
    for a,b in used_edges:
        edges[a][b] = False
        edges[b][a] = False

ans = 0
for i in range(n):
    for j in range(n):
        if edges[i][j]: ans += 1

print(ans//2)
