from collections import deque
import heapq
INF = 10**18

def dijkstra(s, n, g): # s: start, n: |V|, g; glaph (to,cost)
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

r,c=map(int, input().split())
al=[list(map(int, input().split())) for _ in range(r)]
bl=[list(map(int, input().split())) for _ in range(r-1)]


nmax=r*c*2
# r-=1
# c-=1
gl=[[] for _ in range(nmax)]
for y in range(r):
    for x in range(c):
        pos=y*c+x
        if y!=r-1: 
            gl[pos].append((pos+c, bl[y][x]))
        if x!=c-1:
            cost=al[y][x]
            gl[pos].append((pos+1,cost))
            gl[pos+1].append((pos,cost))
        gl[pos].append((pos+r*c,1))
        gl[pos+r*c].append((pos,0))
        if y!=0:
            gl[pos+r*c].append((pos+r*c-c,1))

# print(nmax)
d=dijkstra(0,nmax,gl)
ans=d[r*c-1]
print(ans)
# print(d)