from collections import deque

r, c = map(int, input().split()) 
sy, sx = map(int, input().split()) 
gy, gx = map(int, input().split()) 
sy-=1
sx-=1
gy-=1
gx-=1
maze = []
cost = [ [-1 for _ in range(r)] for _i in range(c) ]

def bps():
    queue = deque()
    queue.append([sy,sx])
    cost[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        for n_y, n_x in [ [y+1,x],[y-1,x],[y,x+1],[y,x-1] ]:
            if n_y>=r or n_x >= c or n_y < 0 or n_x < 0:
                continue
            if maze[n_y][n_x] == '.' and cost[n_y][n_x] == -1:
                cost[n_y][n_x] = cost[y][x] + 1
                queue.append([n_y, n_x])
                # print(cost)

for i in range(r):
    row = list(input())
    maze.append(row)

bps()
print(cost[gy][gx])
