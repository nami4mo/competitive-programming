def dfs(node, visited, g):
    visited[node] = True
    for neib in g[node]:
        if not visited[neib]:
            dfs(neib, visited,g)


N, M = map(int, input().split()) 
abl = []
for _ in range(M):
    a, b = map(int, input().split()) 
    abl.append([a,b])

ans = 0
for i in range(M):
    g = [ [] for _ in range(N+1)]
    for j, ab in enumerate(abl):
        if j == i: continue
        a,b = ab
        g[a].append(b)
        g[b].append(a)
    visited = [False] * (N+1)
    visited[0] = True
    dfs(1, visited, g)
    if False in visited:
        ans+=1 

print(ans)
