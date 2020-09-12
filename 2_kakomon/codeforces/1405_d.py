from collections import deque
import sys
input = sys.stdin.readline

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


for _ in range(int(input())):
    n,a,b,da,db = map(int, input().split())
    if a == b:
        print(('Alice'))
        continue

    gl = [ [] for _ in range(n+1)]
    visited = [-1] * (n+1)
    for i in range(n-1):
        u, v = map(int, input().split()) 
        gl[u].append(v)
        gl[v].append(u)

    node_a = bfs(a, gl, visited)
    # print(visited)
    if visited[b] <= da:
        print('Alice')
        continue

    visited = [-1] * (n+1)
    node_b = bfs(node_a,gl,visited)
    dia = visited[node_b]
    # print(dia)
    db = min(db,dia)
    if db > 2*da:
        print('Bob')
    else:
        print('Alice') 
    # print(visited[node_b])


