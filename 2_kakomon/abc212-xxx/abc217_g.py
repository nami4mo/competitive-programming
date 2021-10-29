MOD=998244353

n,m=map(int, input().split())

dp=[[0]*(n+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(1,n+1):
        cnt=i//m
        dp[i+1][j]=dp[i][j-1]+dp[i][j]*(j-cnt)
        dp[i+1][j]%=MOD
for i in range(1,n+1):
    print(dp[-1][i])