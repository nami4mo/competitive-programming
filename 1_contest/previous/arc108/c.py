import sys
sys.setrecursionlimit(10**6)

def dfs(pare, node, p_to_n, gl, ansl, n):
    if ansl[pare] == p_to_n:
        num = p_to_n - 1
        if num == 0: num = n
        ansl[node] = num
    else:
        ansl[node] = p_to_n
    for next_node, c in gl[node]:
        if ansl[next_node] != -1: continue
        dfs(node, next_node, c, gl ,ansl, n)

n,m = map(int, input().split())
gl = [ [] for _ in range(n+1) ]

for _ in range(m):
    u,v,c = map(int, input().split())
    gl[u].append((v,c))
    gl[v].append((u,c))

ansl = [-1]*(n+1)
dfs(0,1,1,gl,ansl,n)
# print(ansl)
for a in ansl[1:]:
    print(a)