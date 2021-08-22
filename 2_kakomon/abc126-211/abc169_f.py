n,s = map(int, input().split())
al = list(map(int, input().split()))

dp = [ [0]*(s+1) for _ in range(n+1) ]
dp[0][0] = 1

MOD = 998244353
for i in range(n):
    a = al[i]
    for j in range(s+1):
        dp[i+1][j] += dp[i][j]*2
        if j-a >= 0: dp[i+1][j] += dp[i][j-a]
        dp[i+1][j]%=MOD

print(dp[n][s])
