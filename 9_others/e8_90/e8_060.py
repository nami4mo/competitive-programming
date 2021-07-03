from bisect import bisect_left
INF = 10**10

def get_lis(n,al):
    dp = [INF]*(n+1)
    dp[0] = -INF
    res=[0]*(n+1)
    cmax=0
    for i, a in enumerate(al):
        ind = bisect_left(dp, a) # max index of "value <= a"
        dp[ind] = a
        cmax=max(cmax, ind)
        res[i+1]=cmax
    return res

n=int(input())
al=list(map(int, input().split()))
ls=get_lis(n,al)
rs=get_lis(n,al[::-1])

ans=0
for l in range(1,n+1):
    lc=ls[l]
    rc=rs[n-l+1]
    ans=max(ans, lc+rc-1)
print(ans)