n,m=map(int, input().split())
dp=[10**18]*(1<<n)
dp[0]=0
for _ in range(m):
    a,b=map(int, input().split())
    cl=list(map(int, input().split()))
    bit=0
    for c in cl:
        bit+=(1<<(c-1))
    for i in range(1<<n):
        dp[i|bit]=min(dp[i|bit],dp[i]+a)
ans=dp[-1]
if ans==10**18:ans=-1
print(ans)