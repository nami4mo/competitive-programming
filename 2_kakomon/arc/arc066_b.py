n=int(input())
MAX=64
dp=[[0]*3 for _ in range(MAX+1)]
dp[0][0]=1
MOD=10**9+7
for i in range(MAX):
    bit=MAX-i-1
    if n&(1<<bit)>0:
        # 0 0 
        dp[i+1][1]+=dp[i][0]
        dp[i+1][2]+=dp[i][1]
        dp[i+1][2]+=dp[i][2]
        # 0 1 (1 0)
        dp[i+1][0]+=dp[i][0]
        dp[i+1][2]+=dp[i][1]
        dp[i+1][2]+=dp[i][2]
        # 1 1
        # dp[i+1][1]+=dp[i][0]
        dp[i+1][1]+=dp[i][1]
        dp[i+1][2]+=dp[i][2]
    else:
        # 0 0
        dp[i+1][0]+=dp[i][0]
        dp[i+1][2]+=dp[i][1]
        dp[i+1][2]+=dp[i][2]
        # 0 1 (1 0)
        # dp[i+1][0]+=dp[i][0]
        dp[i+1][1]+=dp[i][1]
        dp[i+1][2]+=dp[i][2]
        # 1 1
        # dp[i+1][1]+=dp[i][0]
        dp[i+1][0]+=dp[i][1]
        dp[i+1][2]+=dp[i][2]
    dp[i+1][0]%=MOD
    dp[i+1][1]%=MOD
    dp[i+1][2]%=MOD

ans=sum(dp[-1])%MOD
print(ans)
# print(dp)