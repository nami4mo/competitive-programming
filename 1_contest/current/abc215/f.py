n=int(input())
xyl=[]
for i in range(n):
    x,y=map(int, input().split())
    xyl.append((x,y))
xyl.sort()

from collections import deque
def check(k):
    q=deque(xyl)
    mi,ma=10**10,-1
    for x,y in xyl:
        while q and q[0][0]<=x-k:
            xx,yy=q.popleft()
            mi=min(mi,yy)
            ma=max(ma,yy)
        if y-mi>=k or ma-y>=k:
            return True
    return False


ok, ng = 0, 10**9+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    res = True
    # ...
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)