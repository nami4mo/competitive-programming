k=int(input())
dp=[0]*(k+10)
dp[1]=1
for i in range(2,k+10):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[k],dp[k+1])