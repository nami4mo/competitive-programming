h,w = map(int, input().split())
sl = []
for _ in range(h):
    row = list(input())
    sl.append(row)


dp = [ [10**10]*w for _ in range(h) ]
dp[0][0] = 0
if sl[0][0] == '#': dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i+1 < h:
            if sl[i][j] != sl[i+1][j]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j])
        if j+1 < w:
            if sl[i][j] != sl[i][j+1]:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            else:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j])

if sl[-1][-1] == '#': dp[-1][-1] += 1
print(dp[-1][-1]//2)