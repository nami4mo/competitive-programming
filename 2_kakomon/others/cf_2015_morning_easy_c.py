n,k,m,r=map(int, input().split())
sl=[int(input()) for _ in range(n-1)]+[0]
sl.sort(reverse=True)

target=k*r
csum=sum(sl[:k])
if csum>=target:
    print(0)
else:
    need=target-csum
    ans=sl[k-1]+need
    if ans<=m:print(ans)
    else:print(-1)

