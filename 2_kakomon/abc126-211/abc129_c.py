MOD = 10**9+7

n,m = map(int, input().split())
al = [True]*(n+1)
for _ in range(m):
    al[int(input())] = False

dp = [0]*(n+1) 
dp[0] = 1
for i in range(n):
    if i+2 <= n and al[i+2]:
        dp[i+2] += dp[i]
    if i+1 <= n and al[i+1]:
        dp[i+1] += dp[i]

print(dp[n]%MOD)