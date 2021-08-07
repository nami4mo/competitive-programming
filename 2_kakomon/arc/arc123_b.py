n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cl=list(map(int, input().split()))
al.sort()
bl.sort()
cl.sort()

from collections import deque
# aq=deque(al)
bq=deque(bl)
cq=deque(cl)

ans=0
for a in al:
    while bq and bq[0]<=a:
        bq.popleft()
    if not bq:break
    b=bq.popleft()

    while cq and cq[0]<=b:
        cq.popleft()
    if not cq:break
    cq.popleft()
    ans+=1

print(ans)
