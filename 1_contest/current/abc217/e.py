q=int(input())

from heapq import heappop, heappush
from collections import deque
hq=[]
dq=deque()
for _ in range(q):
    ql=list(map(int, input().split()))
    if ql[0]==1:
        dq.append(ql[1])
    elif ql[0]==2:
        if hq:
            poped=heappop(hq)
            print(poped)
        else:
            poped=dq.popleft()
            print(poped)
    else:
        while dq:
            poped=dq.popleft()
            heappush(hq,poped)
    