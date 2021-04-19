n,m=map(int, input().split())
hl=list(map(int, input().split()))
wl=list(map(int, input().split()))
hl.sort()
wl.sort()

ls=[0]
rs=[0]
for i in range(n//2):
    i1=i*2
    i2=i*2+1
    d=hl[i2]-hl[i1]
    ls.append(ls[-1]+d)
    i1=(n//2-i)*2-1
    i2=(n//2-i)*2
    d=hl[i2]-hl[i1]
    rs.append(rs[-1]+d)

from bisect import bisect_left, bisect_right
ans=10**18
for w in wl:
    i = bisect_right(hl, w) - 1
    if i<0:
        d=hl[0]-w+rs[-1]
    elif i%2==0:
        d=ls[i//2]+w-hl[i]+rs[(n+1)//2-i//2-1]
    else:
        d=ls[i//2+1]+hl[i+1]-w+rs[(n+1)//2-i//2-2]
    ans=min(ans,d)
print(ans)
