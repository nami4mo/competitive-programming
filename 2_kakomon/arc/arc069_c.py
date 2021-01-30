from collections import deque
from heapq import heapify, heappop, heappush
n=int(input())
al=list(map(int, input().split()))

q=deque()
backq=deque()
cmax=0
for i in range(n):
    a=al[i]
    if a>cmax:
        q.append((i,a))
    else:
        backq.append((i,a))
    cmax=max(cmax,a)

cnt=0
ansl=[0]*n
hq=[]
while q:
    i,a=q.pop()
    # print('-----',i,a)
    while backq and backq[-1][0]>i:
        heappush(hq,backq.pop()[1]*(-1))
    
    if not q: # if last
        # cans=(cnt+1)*a
        # while hq:
        #     poped=heappop(hq)
        #     cans+=poped
        # ansl[i]=cans
        # break
        next_a=0
    else:
        next_a=q[-1][1]
    cans=(a-next_a)*cnt
    # print(next_a)
    cans+=a-next_a
    cnt+=1
    while hq and hq[0]*(-1)>=next_a:
        new_a=heappop(hq)*(-1)
        cans+=(new_a-next_a)
        cnt+=1
    ansl[i]=cans

for a in ansl:print(a)