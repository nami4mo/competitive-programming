
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

h,w = map(int, input().split())
g = [ [] for _ in range(h*w) ]
sl = [list(map(int, input().split())) for _ in range(h)]
for y in range(h):
    for x in range(w):
        u = y*w+x
        if y+1<h:
            v = (y+1)*w+x
            g[u].append((v,sl[y+1][x]))
            g[v].append((u,sl[y][x]))            
        if x+1<w:
            v = y*w+x+1
            g[u].append((v,sl[y][x+1]))
            g[v].append((u,sl[y][x]))   

dists_start = dijkstra((h-1)*w, h*w, g)
dists_g1 = dijkstra(h*w-1, h*w, g)
dists_g2 = dijkstra(w-1, h*w, g)

ans = 10**18
for i in range(h*w):
    y = i//w
    x = i%w
    dist = dists_start[i] + dists_g1[i] + dists_g2[i] - sl[y][x]*2
    ans = min(ans, dist)

print(ans)
