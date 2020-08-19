n,m = map(int, input().split())
al = [True]*(n+1)
for _ in range(m):
    a = int(input())
    al[a] = False

MOD = 10**9+7
dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    if i+1 <= n and al[i+1]:
        dp[i+1] += dp[i]
        dp[i+1]%=MOD
    if i+2 <= n and al[i+2]:
        dp[i+2] += dp[i]
        dp[i+2]%=MOD

print(dp[n])
