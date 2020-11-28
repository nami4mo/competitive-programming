
import sys
sys.setrecursionlimit(10**6)
def dfs(v,gl,dl):
    if dl[v] != -1:
        return dl[v]
    dist = 0
    for to in gl[v]:
        d = dfs(to,gl,dl)+1
        dist = max(dist,d)
    dl[v] = dist
    return dist

n,m = map(int, input().split())
gl = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().split())
    u-=1
    v-=1
    gl[u].append(v)

dl = [-1]*(n)
for i in range(n):
    if dl[i] == -1:
        dfs(i,gl,dl)

print(max(dl))