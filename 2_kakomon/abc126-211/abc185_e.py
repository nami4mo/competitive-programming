n,m=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
dp=[[10**18]*(m+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n+1):
    dp[i][0] = i
for j in range(m+1):
    dp[0][j] = j
for i in range(n):
    for j in range(m):
        v = 0 if al[i]==bl[j] else 1
        dp[i+1][j+1] = min(dp[i][j]+v, dp[i][j+1]+1, dp[i+1][j]+1, dp[i+1][j+1])

print(dp[-1][-1])