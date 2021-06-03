k=int(input())
if k%9!=0:
    print(0)
    exit()

dp=[0]*(k+100)
dp[0]=1

MOD=10**9+7
for i in range(k+1):
    for j in range(1,10):
        dp[i+j]+=dp[i]
        dp[i+j]%=MOD

print(dp[k])