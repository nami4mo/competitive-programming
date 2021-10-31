n,m=map(int, input().split())
cal=[]
for _ in range(m):
    a,c=map(int, input().split())
    cal.append((c,a))

cal.sort()
from math import gcd
ans=0
rem=n
for c,a in cal:
    next_rem=gcd(a,rem)
    cnt=rem-next_rem
    ans+=cnt*c
    rem=next_rem

    if rem==1:
        print(ans)
        exit()

if rem!=1:
    print(-1)
else:
    print(ans)