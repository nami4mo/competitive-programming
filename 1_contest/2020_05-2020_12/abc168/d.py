from collections import deque

def bfs(g_list, visited):
    q = deque([1])
    visited[1] = 0
    while q:
        curr_room = q.popleft()
        for next_room in g_list[curr_room]:
            if visited[next_room] >= 0:
                continue
            visited[next_room] = curr_room
            q.append(next_room)


def main():
    n, m = map(int, input().split()) 
    g_list = [ [] for _ in range(n+1)]
    visited = [-1] * (n+1)
    visited[0] = 0
    # print(g_list)
    for i in range(m):
        a, b = map(int, input().split()) 
        g_list[a].append(b)
        g_list[b].append(a)
    bfs(g_list,visited)
    # print(visited)
    ans = visited[2:]
    if -1 in ans:
        print('No')
    else:
        print('Yes')
        for a in ans:
            print(a)

if __name__ == "__main__":
    main()