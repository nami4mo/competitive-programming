from collections import deque

h,w =map(int, input().split())
al = []
alp_d = {chr(ord('a') + i): [] for i in range(26)}

sy,sx = -1,-1
gy,gx = -1,-1

for hi in range(h):
    row = list(input())
    al.append(row)
    for wi in range(w):
        v = row[wi]
        if v == 'S':
            sy,sx = hi,wi
        elif v == 'G':
            gy,gx = hi,wi
        elif v == '#' or v == '.':
            pass
        else:
            alp_d[v].append((hi,wi))

visited = [ [-1]*w for i in range(h)]
q = deque([(sy,sx)])
visited[sy][sx] = 0
alp_used = {chr(ord('a') + i): False for i in range(26)}

# print('ggggg', gy,gx)
# print(al)

ans = -1
while q:
    y, x = q.popleft()
    # print(y,x)
    if (y,x) == (gy,gx):
        ans = visited[gy][gx]
        break
    for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        ny, nx = y+j, x+k
        if ny >= h or nx >= w or ny < 0 or nx < 0:
            continue
        if (al[ny][nx] != '#') and visited[ny][nx] == -1:
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny,nx))
    v = al[y][x]
    # print(v)
    if v != 'S' and v != 'G' and v != '#' and v != '.':
        # print(v)
        if not alp_used[v]:
            # print(v)
            for ny,nx in alp_d[v]:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))
        alp_used[v] = True


print(ans)

# gl = {}
# alps = 'abcdefghijklmnopqrstuvwxyz'
# for a in alps:
#     if len(alp_d[a]) < 2:
#         continue
#     alen = len(alp_d[a])
#     for i in range(alen):
#         for j in range(alen):
#             gl[]

