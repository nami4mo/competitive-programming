# ------------------------ dfs ------------------------
import sys
sys.setrecursionlimit(10**6)

## tree DFS
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



## undirected graph DFS
def dfs(node, visited, g):
    visited[node] = True
    for neib in g[node]:
        if not visited[neib]:
            dfs(neib, visited,g)

N, M = map(int, input().split()) 
g = [ [] for _ in range(n+1)]
for _ in range(M):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)
visited = [False] * (N+1)
visited[0] = True
dfs(1, visited, g)



# ------------------------ bfs ------------------------
## undirected graph BFS
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


## grid map BFS
### calc shortest length of start to goal
from collections import deque
def bfs(sl, visited, sy, sx, gy, gx, h, w):
    q = deque([[sy,sx]])
    visited[sy][sx] = 0
    while q:
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[gy][gx]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            ny, nx = y+j, x+k
            if ny >= h or nx >= w or ny < 0 or nx < 0:
                continue
            if sl[ny][nx] == '.' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny,nx])
                print(ny,nx, visited[ny][nx])
    return -1

h, w = map(int, input().split()) 
sl = [list(input()) for _ in range(h)]
visited = [ [-1]*w for i in range(h)]


# --------- dikstra ------------
import heapq
def dijkstra(s, n, g):
    INF = 10**10
    d = [INF] * n
    d[s] = 0
    que = [] # (a,b): a... shortest dist, b... v
    heapq.heapify(que)
    heapq.heappush(que, (0, s))

    while que:
        dist, v = heapq.heappop(que)
        if d[v] < dist: continue # if v has been already used -> continue
        for edge in g[v]:
            to, cost = edge
            if d[to] > d[v] + cost:
                d[to] = d[v] + cost
                heapq.heappush(que, (d[to], to))
    return d

v,e,s = map(int, input().split())
g = [ [] for _ in range(v)]
for _ in range(e):
    s,t,d = map(int, input().split())
    g[s].append((t,d))
ans = dijkstra(s, v, g)



def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d