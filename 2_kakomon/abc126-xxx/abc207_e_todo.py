MOD=10**9+7
n=int(input())
al=list(map(int, input().split()))

dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[1][i]=1

for i in range(2,n+1):
    mc=[0]*i
    mc[0]=1
    csum=0
    for j in range(1,n+1):
        csum+=al[i-1]
        csum%=i
        dp[i][j]+=mc[csum]
        mc[csum]+=dp[i-1][j]
        mc[csum]%=MOD