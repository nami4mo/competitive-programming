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
    

def main():
    n,u,v = map(int, input().split())
    gl = [ [] for _ in range(n+1)]
    visited_u = [-1] * (n+1)
    visited_v = [-1] * (n+1)
    for i in range(n-1):
        a, b = map(int, input().split()) 
        gl[a].append(b)
        gl[b].append(a)
    bfs(u, gl, visited_u)
    bfs(v, gl, visited_v)

    # print(visited_u)
    # print(visited_v)

    # target_i = 0
    # max_diff_v = 0
    ans = 0
    for i in range(1,n+1):
        if visited_u[i] < visited_v[i] and visited_v[i]:
            # if (visited_v[i]-visited_u[i])%2 == 0:
            val = visited_v[i]-1
            ans = max(ans,val)
            # else:
                # val = visited_v[i]
                # ans = max(ans,val)
    print(ans)



if __name__ == "__main__":
    main()