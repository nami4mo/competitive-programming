n=int(input())
al=list(map(int, input().split()))
bl=list(map(int, input().split()))
cl=[]
ans=0
for i in range(n):
    cl.append((al[i]-bl[i],i))
    ans+=max(al[i],bl[i])
cl.sort(reverse=True)

sq0=[]
sq1=[]
tq0=[]
tq1=[]
for v,i in cl:
    if v>=0:
        if i%2==0:sq0.append(v)
        else:sq1.append(v)
    else:
        if i%2==0:tq0.append(-v)
        else:tq1.append(-v)

sq0.sort()
sq1.sort()
tq0.sort()
tq1.sort()
from collections import deque
sq0=deque(sq0)
sq1=deque(sq1)
tq0=deque(tq0)
tq1=deque(tq1)

c0,c1=len(sq0),len(sq1)
while c0!=c1:
    if c0>c1:
        if not tq1:
            p=sq0.popleft()
            ans-=p
            c0-=1
        else:
            if sq0[0] < tq1[0]:
                p=sq0.popleft()
                ans-=p
                c0-=1
            else:
                p=tq1.popleft()
                ans-=p
                c1+=1
    else:
        if not tq0:
            p=sq1.popleft()
            ans-=p
            c1-=1
        else:
            if sq1[0] < tq0[0]:
                p=sq1.popleft()
                ans-=p
                c1-=1
            else:
                p=tq0.popleft()
                ans-=p
                c0+=1
print(ans)