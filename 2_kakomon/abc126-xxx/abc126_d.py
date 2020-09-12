import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(curr_v, pare_v, curr_sum, visited, g):
    if curr_sum%2 == 0:
        visited[curr_v] = 0
    else:
        visited[curr_v] = 1
    for neib_vw in g[curr_v]:
        if neib_vw[0] == pare_v: continue
        dfs(neib_vw[0], curr_v, curr_sum+neib_vw[1], visited, g)
    

N = int(input())
g = [ [] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(N-1):
    u, v, w = map(int, input().split()) 
    w%=2
    g[u].append((v,w))
    g[v].append((u,w))

dfs(1, -1, 0, visited, g)
for p in visited[1:]:
    print(p)
    

