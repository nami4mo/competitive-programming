n,m = map(int, input().split())
ball_cnts = [1]*(n+1)
ball_cnts[0] = 0
red_flag = [False]*(n+1)
red_flag[1] = True

for _ in range(m):
    x,y = map(int, input().split())
    if red_flag[x]:
        red_flag[y] = True
    if ball_cnts[x] == 1:
        red_flag[x] = False
    ball_cnts[x] -= 1
    ball_cnts[y] += 1

ans = 0
for v in red_flag:
    if v: ans += 1

print(ans)