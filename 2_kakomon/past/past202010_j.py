import heapq
def dijkstra(s, n, g): # s: start, n: |V|, g; glaph 
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


n,m = map(int, input().split())
xab,xac,xbc = map(int, input().split())
s = input()

if s[0] == 'B':
    s = s.replace('B','a').replace('A','B').replace('a','A')
    xac,xbc = xbc,xac
elif s[0] == 'C':
    s = s.replace('C','a').replace('A','C').replace('a','A')
    xab,xbc = xbc,xab


g = [ [] for _ in range(n)]
for _ in range(m):
    a,b,d = map(int, input().split())
    g[a-1].append((b-1,d))
    g[b-1].append((a-1,d))

dists = dijkstra(0, n, g)


for i in range(n):
    if s[i] == 'B':
        g[0].append((i,xab))
    elif s[i] == 'C':
        g[0].append((i,xac))


min_bv = 10**18
min_bi = -1
min_cv = 10**18
min_ci = -1
for i in range(n):
    if s[i] == 'B':
        if min_bv > dists[i]:
            min_bv = dists[i]
            min_bi = i
    elif s[i] == 'C':
        if min_cv > dists[i]:
            min_cv = dists[i]
            min_ci = i
    
if min_bi != -1:
    for i in range(n):
        if s[i] == 'A':
            g[min_bi].append((i,xab))
        elif s[i] == 'C':
            g[min_bi].append((i,xbc))

if min_ci != -1:
    for i in range(n):
        if s[i] == 'A':
            g[min_ci].append((i,xac))
        elif s[i] == 'B':
            g[min_ci].append((i,xbc))

dists = dijkstra(0, n, g)
print(dists[n-1])