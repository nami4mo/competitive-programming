n=int(input())
s=input()
from collections import deque
oq=deque()
xq=deque()
for i in range(n):
    if s[i]=='o':oq.append(i)
    else:xq.append(i)

ans=0
for i in range(n):
    if s[i]=='o':
        oq.popleft()
        if not xq:continue
        mi=xq[0]
        ans+=(n-mi)
    else:
        xq.popleft()
        if not oq:continue
        mi=oq[0]
        ans+=(n-mi)
    
print(ans)