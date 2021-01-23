n,m=map(int, input().split())
fl=[int(input()) for _ in range(n)]
lastms=[0]*(m+1)
dp=[-1]*(n+1)
dp[0]=1
sdp=[0,1]
MOD=10**9+7

samei=0
for i in range(n):
    f=fl[i]
    last=lastms[f]
    lastms[f]=i+1
    samei=max(samei,last)
    left=sdp[samei]
    dp[i+1]=sdp[i+1]-left
    dp[i+1]%=MOD
    sdp.append( (sdp[i+1]+dp[i+1])%MOD )
print(dp[-1]%MOD)