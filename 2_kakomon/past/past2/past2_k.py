n = int(input())
s = input()
cl = list(map(int, input().split()))
dl = list(map(int, input().split()))

INF = 10**18
dp = [[INF]*(n+1) for _ in range(n+1)]

dp[0][0] = 0
for i in range(n):
    if s[i] == '(':
        for j in range(n):
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+dl[i])
            if j > 0: dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j]+cl[i])
    else:
        for j in range(n):
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+cl[i])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+dl[i])
            if j > 0: dp[i+1][j-1] = min(dp[i+1][j-1], dp[i][j])

print(dp[n][0])