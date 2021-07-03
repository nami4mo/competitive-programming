n=int(input())
al=list(map(int, input().split()))
ts=sum(al)
al=al+al
if ts%10!=0:
    print('No')
    exit()
t=ts//10

c=0
from collections import deque
q=deque()
for a in al:
    while c>t:
        poped=q.popleft()
        c-=poped
    if c==t:
        print('Yes')
        exit()
    q.append(a)
    c+=a
    if c==t:
        print('Yes')
        exit()
print('No')