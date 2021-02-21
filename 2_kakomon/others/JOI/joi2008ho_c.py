n,m=map(int, input().split())
al=[int(input()) for _ in range(n)]+[0]
pl=[]
for a in al:
    for a2 in al:
        pl.append(a+a2)

pl.sort()
ans=0
from bisect import bisect_left, bisect_right
for p in pl:
    if p>m:break
    ind = bisect_right(pl, m-p) - 1
    if ind<0:break
    v=pl[ind]
    ans=max(ans,v+p)
print(ans)