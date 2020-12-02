import sys
sys.setrecursionlimit(10**6)
def dfs(pare, v, hl, gl):
    dist = 0
    for neib in gl[v]:
        if neib == pare: continue
        dist += (dfs(v, neib, hl, gl)+1)
    if dist == 0:
        if hl[v] == 0: return -1
        else: return 0
    return dist

n,x = map(int, input().split())
x-=1
hl = list(map(int, input().split()))
gl = [[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

ans = dfs(-1,x,hl,gl)*2
print(max(ans,0))