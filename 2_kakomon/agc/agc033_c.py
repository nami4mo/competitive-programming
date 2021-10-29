from collections import deque
def bfs(start, g, visited):
    q = deque([start])
    visited[start] = 0
    last_node = 0
    while q:
        curr_node = q.popleft()
        for next_node in g[curr_node]:
            if visited[next_node] >= 0: continue
            visited[next_node] = visited[curr_node] + 1
            q.append(next_node)
            last_node = next_node
    return last_node

n = int(input())
gl = [ [] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split()) 
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

visited = [-1] * (n)
node_a = bfs(0, gl, visited)
visited = [-1] * (n)
node_b = bfs(node_a,gl,visited)
# print(visited[node_b])
# print(node_a, node_b)
diam=visited[node_b]+1
# print(diam)
if diam%3==2:print('Second')
else:print('First')