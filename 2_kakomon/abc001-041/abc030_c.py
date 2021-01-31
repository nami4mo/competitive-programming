n,m=map(int, input().split())
x,y=map(int, input().split())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
from collections import deque
aq=deque(al)
bq=deque(bl)

t=0
ans=0
while True:
    while aq and aq[0]<t:
        aq.popleft()
    if not aq:break
    t=aq.popleft()
    t+=x
    while bq and bq[0]<t:
        bq.popleft()
    if not bq:break
    t=bq.popleft()
    t+=y
    ans+=1
print(ans)