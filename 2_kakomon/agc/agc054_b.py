n=int(input())
al=list(map(int, input().split()))
asum=sum(al)
if asum%2==1:
    print(0)
    exit()

MOD=998244353
dp=[[0]*(asum//2+1) for _ in range(n+1)]
dp[0][0]=1
for a in al:
    new_dp=[[0]*(asum//2+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(asum//2+1):
            new_dp[i][j]+=dp[i][j]
            new_dp[i][j]%=MOD
            if j+a<=asum//2 and i+1<n+1:
                new_dp[i+1][j+a]+=dp[i][j]
                new_dp[i+1][j+a]%=MOD

    for i in range(n+1):
        for j in range(asum//2+1):
            dp[i][j]=new_dp[i][j]

facs=[1]
for i in range(n):
    facs.append((facs[-1]*(i+1))%MOD)

ans=0
for c1 in range(1,n+1):
    c2=n-c1
    ans+=facs[c1]*facs[c2]*dp[c1][asum//2]
    ans%=MOD
print(ans)