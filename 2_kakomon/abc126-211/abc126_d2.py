import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start,n,g):
    visited = [-1]*(n+1)
    visited[start] = 0
    stack = deque([start])
    while stack:
        c_node = stack.pop()
        for neib, dist in g[c_node]:
            if visited[neib] != -1: continue
            visited[neib] = visited[c_node] + dist
            stack.append(neib)
    return visited
    

N = int(input())
g = [ [] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(N-1):
    u, v, w = map(int, input().split()) 
    w%=2
    g[u].append((v,w))
    g[v].append((u,w))

visited = dfs(1,N,g)
for p in visited[1:]:
    print(p%2)
    

