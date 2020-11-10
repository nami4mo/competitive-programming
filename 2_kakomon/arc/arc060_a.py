n,a = map(int, input().split())
xl_ = list(map(int, input().split()))
xl = [x-a for x in xl_]

dp = [ {} for _ in range(n+1) ]
for i in range(n+1):
    for j in range(-2500,2501):
        dp[i][j] = 0

dp[0][0] = 1
for i in range(n):
    x = xl[i]
    for j in range(-2500,2501):
        dp[i+1][j] += dp[i][j]
        if -2500 <= j+x <= 2500:
            dp[i+1][j+x] += dp[i][j]

print(dp[n][0]-1)