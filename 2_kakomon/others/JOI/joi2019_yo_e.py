n,m=map(int, input().split())
al=list(map(int, input().split()))
backs=[i for i in range(n)]
for _ in range(m):
    l,r=map(int, input().split())
    l-=1
    r-=1
    backs[r]=min(l,backs[r])

# print(backs)

cmin=n-1
for i in range(n-1,-1,-1):
    cmin=min(cmin,backs[i])
    backs[i]=cmin

# print(backs)
dp=[0]*n
dp[0]=al[0]
cmax=al[0]
for i in range(1,n):
    if backs[i]==0: prev_max=0
    else: prev_max=dp[backs[i]-1]
    dp[i]=max(cmax,prev_max+al[i])
    cmax=max(cmax,dp[i])
print(dp[-1])