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
                # prev_vl[next_v] = v
                heapq.heappush(que, (d[next_v], next_v))
    return d


n,m=map(int, input().split())
s,t=map(int, input().split())
s-=1
t-=1
gl=[[] for _ in range(n)]
for _ in range(m):
    x,y,d=map(int, input().split())
    x-=1
    y-=1
    gl[x].append((y,d))
    gl[y].append((x,d))

d1=dijkstra(s,n,gl)
d2=dijkstra(t,n,gl)
for i in range(n):
    if d1[i]==d2[i] and d1[i]<=10**10:
        print(i+1)
        break
else:
    print(-1)