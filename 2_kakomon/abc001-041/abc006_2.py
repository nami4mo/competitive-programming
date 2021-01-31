MOD=10007
n=int(input())
dp=[0]*(1000001)
dp[2]=1
for i in range(3,n):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i]%=MOD
print(dp[n-1])