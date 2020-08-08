from collections import deque
MOD = 10**9+7

def bfs(start, goal, g, visited,n):
    q = deque([start])
    visited[start] = 1
    dist = [-1]*(n+1)
    while q:
        curr_node = q.popleft()
        if curr_node == goal: return
        for next_node in g[curr_node]:
            if dist[next_node] == -1 or dist[curr_node]+1 == dist[next_node]:
                visited[next_node] += visited[curr_node]
                visited[next_node]%=MOD
            if dist[next_node] >= 0: continue
            dist[next_node] = dist[curr_node] + 1
            q.append(next_node)
        # print(curr_node, visited)


n = int(input())
a,b = map(int, input().split())
m = int(input())
gl = [ [] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split()) 
    gl[x].append(y)
    gl[y].append(x)

bfs(a, b, gl, visited,n)
print(visited[b])
# print(visited)
