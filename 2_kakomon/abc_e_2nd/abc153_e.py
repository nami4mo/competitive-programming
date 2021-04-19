h,n=map(int, input().split())
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    abl.append((a,b))

INF=10**18
MAX=h+10**4+10
dp=[INF]*(MAX)
dp[0]=0
for i in range(h):
    for a,b in abl:
        dp[i+a]=min(dp[i+a], dp[i]+b)

ans=INF
for i in range(h,MAX):
    ans=min(ans,dp[i])
print(ans)