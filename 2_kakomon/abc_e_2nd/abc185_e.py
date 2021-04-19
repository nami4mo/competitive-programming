n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
INF=10**10
dp=[[INF]*(m+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n+1):dp[i][0]=i
for j in range(m+1):dp[0][j]=j
for i in range(1,n+1):
    for j in range(1,m+1):
        if al[i-1]==bl[j-1]:
            dp[i][j]=min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
        else:
            dp[i][j]=min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
print(dp[n][m])