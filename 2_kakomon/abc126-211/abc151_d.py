from collections import deque
import sys
input = sys.stdin.readline

def bfs(s_l, sy, sx, h, w):
    visited = [ [-1]*w for i in range(h)]
    q = deque([[sy,sx]])
    visited[sy][sx] = 0
    last_dist = -1
    while q:
        y, x = q.popleft()
        # if [y, x] == [gy, gx]:
        #     return visited[gy][gx]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            n_y, n_x = y+j, x+k
            if n_y >= h or n_x >= w or n_y < 0 or n_x < 0:
                continue
            if s_l[n_y][n_x] == '.' and visited[n_y][n_x] == -1:
                visited[n_y][n_x] = visited[y][x] + 1
                last_dist = visited[n_y][n_x]
                q.append([n_y,n_x])
    return last_dist

def main():
    h, w = map(int, input().split()) 
    s_l = []
    all_dot_cnt = 0
    for i in range(h):
        row = list(input())
        s_l.append(row)
        all_dot_cnt += row.count('.')
    
    curr_ans = -1
    visited = [ [-1]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if s_l[i][j] == '.':
                res = bfs(s_l, i, j, h, w)
                if res > curr_ans:
                    curr_ans = res
    print(curr_ans)

if __name__ == "__main__":
    main()