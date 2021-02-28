n=int(input())
# al=list(map(int, input().split()))
al=[int(input()) for _ in range(n)]
s=sum(al)
sh=(s+1)//2

MOD=998244353
dp=[[0]*(s+1) for _ in range(n+1)]
dph=[[0]*(s+1) for _ in range(n+1)]
dp[0][0]=1
dph[0][0]=1
for i in range(n):
    a=al[i]
    for j in range(s+1):
        v=j+a
        if v<=s: 
            dp[i+1][v]+=dp[i][j]
            dp[i+1][v]%=MOD
            dph[i+1][v]+=dph[i][j]
            dph[i+1][v]%=MOD
        dp[i+1][j]+=dp[i][j]*2
        dp[i+1][j]%=MOD
        dph[i+1][j]+=dph[i][j]
        dph[i+1][j]%=MOD

notans=0
for i in range(sh,s+1):
    notans+=dp[n][i]
if s%2==0:notans-=dph[n][s//2]
notans*=3
allcomb=pow(3,n,MOD)
ans=allcomb-notans
print(ans%MOD)