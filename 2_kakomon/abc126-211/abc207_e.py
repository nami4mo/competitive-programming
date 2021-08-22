n=int(input())
al=list(map(int, input().split()))


# dp[i][j]: i個みてj個のblockができている 組み合わせ
dp=[[0]*(n+1) for _ in range(n+1)]
dp[0][0]=1

# sdp[i][j]: 現在までで、sum(al)をiで割ったあまりがjになるdpの累積わ
sdp=[[0]*(n+1) for _ in range(n+1)]
sdp[0][0]=1
sdp[1][0]=1

csum=[0]
for a in al:
    csum.append(csum[-1]+a)
MOD=10**9+7
for i in range(n):
    for j in range(1,n+1):
        # i+1個見てj分割
        dp[i+1][j]+=sdp[j][csum[i+1]%j]
        dp[i+1][j]%=MOD
    for j in range(1,n+1):
        sdp[j][csum[i+1]%j]+=dp[i+1][j-1]
        sdp[j][csum[i+1]%j]%=MOD
# print(dp)
ans=sum(dp[n])%MOD
print(ans)