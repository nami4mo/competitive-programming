n,k = map(int, input().split())
al = list(map(int, input().split()))

dp=[[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
MOD = 10**9+7
for i in range(n):
    cumsums = []
    v = 0
    for j in range(k+1):
        v += dp[i][j]
        v%=MOD
        cumsums.append(v)

    a = al[i]
    for j in range(k+1):
        # dp[i+1][j] = sum( dp[i][j-a] ~ dp[i][j])
        r = cumsums[j]
        l = cumsums[j-a-1] if j-a > 0 else 0
        dp[i+1][j] += (r-l)
        dp[i+1][j] %= MOD

print(dp[n][k])