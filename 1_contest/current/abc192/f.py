n,x=map(int, input().split())
al=list(map(int, input().split()))

from copy import copy, deepcopy

ans=10**18
for k in range(1,n+1):
    need_rem=x%k
    dp=[[-1]*102 for _ in range(102)]
    dp[0][0]=0
    for i in range(n):
        new_dp=[[-1]*k for _ in range(k+2)]
        a=al[i]
        for j in range(k+1):
            for r in range(k):
                if dp[j][r]==-1:continue
                new_dp[j][r]=max(new_dp[j][r], dp[j][r])
                new_dp[j+1][(r+a)%k]=max(new_dp[j+1][(r+a)%k], dp[j][r]+a)
        dp=copy(new_dp)
        # for j in range(k+1):
        #     for r in range(k):
        #         dp[j][r]=new_dp[j][r]
    dmax=dp[k][need_rem]
    if dmax==-1:continue
    cnt=(x-dmax)//k
    ans=min(ans,cnt)

print(ans)