m,n=map(int, input().split())
ml=[int(input()) for _ in range(m)]
ml.sort(reverse=True)

INF=10**18
dp=[INF]*(m+1)
dp[0]=0
for _ in range(n):
    c,e=map(int, input().split())
    new_dp=dp[:]
    for j in range(m+1):
        new_dp[min(j+c,m)]=min(new_dp[min(j+c,m)], dp[j]+e)
    dp=new_dp[:]
ans=0
manju=0
for i in range(1,m+1):
    box=dp[i]
    manju+=ml[i-1]
    ans=max(ans,manju-box)

print(ans)