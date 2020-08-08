from collections import deque

def bfs(s_l, visited, sy, sx, gy, gx, h, w):
    q = deque([[sy,sx]])
    visited[0][0] = 0
    while q:
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[gy][gx]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            n_y, n_x = y+j, x+k
            if n_y >= h or n_x >= w or n_y < 0 or n_x < 0:
                continue
            if s_l[n_y][n_x] == '.' and visited[n_y][n_x] == -1:
                visited[n_y][n_x] = visited[y][x] + 1
                q.append([n_y,n_x])
    return -1

def main():
    h, w = map(int, input().split()) 
    s_l = []
    all_dot_cnt = 0
    for i in range(h):
        row = list(input())
        s_l.append(row)
        all_dot_cnt += row.count('.')
    
    visited = [ [-1]*w for i in range(h)]
    res = bfs(s_l, visited, 0, 0, h-1, w-1, h, w)
    if res == -1:
        print(-1)
    else:
        # print(res)
        # print(all_dot_cnt)
        print(all_dot_cnt-res-1)

if __name__ == "__main__":
    main()