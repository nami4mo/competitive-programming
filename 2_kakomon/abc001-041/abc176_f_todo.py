n=int(input())
al=list(map(int, input().split()))
al=[a-1 for a in al]
dp=[[0]*(n) for _ in range(n)]

cnt=0
maxl=[0]*(n)
for i in range(n-1):
    d,e,f=al[3*i+2],al[3*i+3],al[3*i+4]
    defl=[d,e,f]
    defl.sort()
    d,e,f=defl
    if d==e and e==f:
        cnt+=1
        continue
    if d!=e and e!=f and f!=d:
        dp[e][f]=max(dp[e][f],dp[d][d]+1)
        dp[f][e]=max(dp[f][e],dp[d][d]+1)
        dp[f][d]=max(dp[f][d],dp[e][e]+1)
        dp[d][f]=max(dp[d][f],dp[e][e]+1)
        dp[d][e]=max(dp[d][e],dp[f][f]+1)
        dp[e][d]=max(dp[e][d],dp[f][f]+1)
        for j in range(n):
            dp[j][d]=max(dp[j][d],maxl[j])
            dp[j][e]=max(dp[j][e],maxl[j])
            dp[j][f]=max(dp[j][f],maxl[j])
            dp[d][j]=max(dp[d][j],maxl[j])
            dp[e][j]=max(dp[e][j],maxl[j])
            dp[f][j]=max(dp[f][j],maxl[j])

    elif d==e:
        for j in range(n):
            dp[j][f]=max(dp[d][j]+1,dp[j][d]+1,dp[j][f])
            dp[f][j]=max(dp[d][j]+1,dp[j][d]+1,dp[f][j])
        dp[d][d]=max(dp[d][d],dp[f][f]+1)
        for j in range(n):
            dp[j][d]=maxl[j]
            dp[d][j]=maxl[j]
            if j!=d:
                dp[j][f]=maxl[j]
                dp[f][j]=maxl[j]
            else:
                dp[j][f]=maxl[j]
                dp[f][j]=maxl[j]

    else:
        d,f=f,d
        for j in range(n):
            dp[j][f]=max(dp[d][j]+1,dp[j][d]+1,dp[j][f])
            dp[f][j]=max(dp[d][j]+1,dp[j][d]+1,dp[f][j])
        dp[d][d]=max(dp[d][d],dp[f][f]+1)
        for j in range(n):
            dp[j][d]=maxl[j]
            dp[d][j]=maxl[j]
            if j!=d:
                dp[j][f]=maxl[j]
                dp[f][j]=maxl[j]
            else:
                dp[j][f]=maxl[j]
                dp[f][j]=maxl[j]

        for j in range(n):
            maxl[j]=max(dp[j][d],dp[j][e],dp[j][f],maxl[j])
            maxl[j]=max(dp[d][j],dp[e][j],dp[f][j],maxl[j])

ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans,dp[i][j])
print(ans+cnt)
print(dp)