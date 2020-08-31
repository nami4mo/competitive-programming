'''
    [DFS]
'''
import sys
sys.setrecursionlimit(10**6)

## ---------- tree DFS ----------
def dfs(curr, pare, g):
    for chi in g[curr]:
        if chi == pare: continue
        # any processing here
        dfs(chi, curr, g)

n = int(input())
g = [ [] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)
dfs(1, -1, g)


## ---------- undirected graph DFS ----------
def dfs(node, visited, g):
    visited[node] = True
    for neib in g[node]:
        if not visited[neib]:
            dfs(neib, visited,g)

n, m = map(int, input().split()) 
g = [ [] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)
visited = [False] * (n+1)
visited[0] = True
dfs(1, visited, g)



'''
    [BFS]
'''
## ---------- undirected graph BFS ----------
### calc shortest length for each node 
from collections import deque
def bfs(start, g, visited):
    q = deque([start])
    visited[start] = 0
    while q:
        curr_node = q.popleft()
        for next_node in g[curr_node]:
            if visited[next_node] >= 0: continue
            visited[next_node] = visited[curr_node] + 1
            q.append(next_node)

n, m = map(int, input().split()) 
gl = [ [] for _ in range(n+1)]
visited = [-1] * (n+1)
for i in range(m):
    a, b = map(int, input().split()) 
    gl[a].append(b)
    gl[b].append(a)
bfs(1, gl, visited)


## ---------- grid map BFS ----------
### calc shortest length of start to goal
from collections import deque
def bfs(sl, visited, sy, sx, gy, gx, h, w):
    q = deque([(sy,sx)])
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if (y,x) == (gy,gx):
            return visited[gy][gx]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ny, nx = y+j, x+k
            if ny >= h or nx >= w or ny < 0 or nx < 0:
                continue
            if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))
    return -1

h, w = map(int, input().split()) 
sl = [list(input()) for _ in range(h)]
visited = [ [-1]*w for i in range(h)]

## --------- 01-BFS ---------
# https://atcoder.jp/contests/abc176/tasks/abc176_d
# abc176_d2.py


'''
    [dikstra] 
    - 単一始点用（1 対 全）/負の辺があるときは使用不可
    - O(|E|*|logV|)... 全ノードが繋がっているとき(|E|=|V|**2)などは要注意
'''
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

v,e,s = map(int, input().split())
g = [ [] for _ in range(v+1)]
for _ in range(e):
    s,t,d = map(int, input().split())
    g[s].append((t,d))
ans = dijkstra(s, v+1, g)



'''
    [warshall_floyd]
'''
def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d



'''
    [bellman_ford]
'''
# g...  list of edges [ (from,to,cost), (from,to,cost), ...]
# 負の閉路がゴールにたどりつくか判定するには、n-1回のループの後、距離更新時にINFを伝搬させるループをさらにn-1回行う (abc061_d)
# もしくは、ゴールから逆順に辿った頂点 と スタートから辿った頂点 の＆をとって、不要な頂点（ゴールにたどり着かない閉路）を消す
def bellman_ford(s, n, g): # s: start, n: |V|, g; glaph 
    INF = 10**18
    d = [INF]*n
    d[s] = 0
    for i in range(n): # max n-1 loops. if update d[] in n-th loop -> negative cycle
        update = False
        for v_from, v_to, cost in g:
            if d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost
                update = True
        if not update:
            return d
    else: # if not break until n-th loop -> detect negative cycle
        # may do something for negatice cycle
        return None

