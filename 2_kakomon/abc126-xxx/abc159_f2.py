n,s = map(int, input().split())
al = list(map(int, input().split()))

MOD = 998244353
dp = [ [0]*(s+3001) for _ in range(n+1)]
dp_l = [ [0]*(s+3001) for _ in range(n+1)]
dp_lr = [ [0]*(s+3001) for _ in range(n+1)]

dp[0][0] = 1

ans = 0
for i,a in enumerate(al):
    for j in range(s+1):
        dp[i+1][j] += dp[i][j]
        dp_l[i+1][j+a] += dp[i][j]*(i+1)
        dp_lr[i+1][j+a] += dp[i][j]*(i+1)*(n-i)

        dp_l[i+1][j] += dp_l[i][j]
        dp_l[i+1][j+a] += dp_l[i][j]
        dp_lr[i+1][j+a] += dp_l[i][j]*(n-i)

        dp_lr[i+1][j] += dp_lr[i][j]

        dp[i+1][j]%=MOD
        dp[i+1][j+a]%=MOD
        dp_l[i+1][j]%=MOD
        dp_l[i+1][j+a]%=MOD
        dp_lr[i+1][j]%=MOD
        dp_lr[i+1][j+a]%=MOD


ans = dp_lr[n][s]
print(ans)