n,k=map(int, input().split())
al=list(map(int, input().split()))

dp=[[0]*(k+1) for _ in range(n+1)]
dp[0][0]=1

MOD=10**9+7
for i in range(n):
    sdp=[0]*(k+2)
    for j in range(1,k+2):
        sdp[j]=sdp[j-1]+dp[i][j-1]
    for j in range(k+1):
        dp[i+1][j] = sdp[j+1]-sdp[max(0,j-al[i])]
        dp[i+1][j]%=MOD

print(dp[-1][k])