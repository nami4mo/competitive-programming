n=int(input())
al=[int(input()) for _ in range(n)]
INF=10**18
dp=[[INF]*(n+1) for _ in range(5)]
dp[0][0]=0
dp[1][0]=0
dp[2][0]=0
dp[3][0]=0
dp[4][0]=0

for i in range(n):
    dp[0][i+1]=dp[0][i]+al[i]

for i in range(n):
    v=al[i]%2
    if al[i]==0:v=2
    dp[1][i+1]=min(dp[1][i+1],dp[1][i]+v, dp[0][i]+v, dp[0][i+1])

for i in range(n):
    dp[2][i+1]=min(dp[2][i+1],dp[2][i]+(al[i]+1)%2, dp[1][i]+(al[i]+1)%2, dp[1][i+1])

for i in range(n):
    v=al[i]%2
    if al[i]==0:v=2
    dp[3][i+1]=min(dp[3][i+1],dp[3][i]+v, dp[2][i]+v, dp[2][i+1])

for i in range(n):
    dp[4][i+1]=min(dp[4][i+1],dp[4][i]+al[i], dp[3][i]+al[i], dp[3][i+1])

# print(dp)
print(dp[4][n])