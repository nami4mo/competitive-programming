
import sys
input = sys.stdin.readline
n,m,k=map(int, input().split())
uvl=[]
for _ in range(m):
    u,v=map(int, input().split())
    u-=1
    v-=1
    uvl.append((u,v))

dp=[0]*n
dp[0]=1
MOD=998244353
for i in range(k):
    csum=0
    for v in dp:
        csum+=v
        csum%=MOD
    new_dp=[csum]*n
    # print(new_dp)
    for j in range(n):
        new_dp[j]-=dp[j]
    for u,v in uvl:
        new_dp[u]-=dp[v]
        new_dp[v]-=dp[u]
        new_dp[u]%=MOD
        new_dp[v]%=MOD

    dp=new_dp[:]

ans=dp[0]%MOD
print(ans)