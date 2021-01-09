from collections import deque

n,k=map(int, input().split())
al=list(map(int, input().split()))
aq=deque(al)
inq=deque()
outq=deque()

insum=0
for i in range(k):
    poped=aq.popleft()
    insum+=poped
    inq.append(poped)

outsum=0 # only pos. val
for i in range(n-k):
    poped=aq.popleft()
    outsum+=max(0,poped)
    outq.append(poped)

ans=max(0,max(0,insum)+outsum)
for i in range(n-k):
    poped=inq.popleft()
    insum-=poped
    outsum+=max(0,poped)
    
    poped2=outq.popleft()
    outsum-=max(0,poped2)
    insum+=poped2
    inq.append(poped2)

    ans=max(ans, max(0,insum)+outsum)
print(ans)