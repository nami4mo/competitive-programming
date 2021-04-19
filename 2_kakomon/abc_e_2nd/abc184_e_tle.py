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

import sys
input = sys.stdin.readline

h,w=map(int, input().split())
sl=[list(input()) for _ in range(h)]

start=-1
goal=-1

gl=[[] for _ in range(h*w+26)]
for i in range(h):
    for j in range(w):
        v=sl[i][j]
        if v=='#':continue
        pos=i*w+j
        if v=='S':start=pos
        elif v=='G':goal=pos
        elif v=='.':pass
        else:
            ci=ord(v)-ord('a')
            gl[pos].append((h*w+ci,1))
            gl[h*w+ci].append((pos,0))
        for dy,dx in [(1,0),(0,1)]:
            yy=i+dy
            xx=j+dx
            if not (0<=yy<h and 0<=xx<w): continue
            if sl[yy][xx]=='#':continue
            ppos=yy*w+xx
            gl[pos].append((ppos,1))
            gl[ppos].append((pos,1))

d=dijkstra(start,h*w+26,gl)
ans=d[goal]
if ans>=10**18:ans=-1
print(ans)