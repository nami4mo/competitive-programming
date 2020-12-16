n,s=map(int, input().split())
al=list(map(int, input().split()))

dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1
ans = 0
MOD = 998244353
for i in range(n):
    a = al[i]
    # if a>s:continue
    if a<=s:
        dp[i+1][a] += (i+1)
    if a==s:
        ans += (i+1)*(n-i)
        ans %= MOD
    for j in range(1,s):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= MOD
        if j+a <= s:
            dp[i+1][j+a] += dp[i][j]
            dp[i+1][j+a] %= MOD
        if j+a == s:
            ans += dp[i][j]*(n-i)
            ans %= MOD

print(ans%MOD)