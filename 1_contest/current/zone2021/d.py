ans=500**2*3
ans+=250*501*500
print(ans)

s=list(input())
from collections import deque
q=deque()
flip=False

for si in s:
    if si=='R':
        flip=not flip
    else:
        if not flip:
            q.append(si)
            while len(q)>=2 and q[-1]==q[-2]:
                q.pop()
                q.pop()
        else:
            q.appendleft(si)
            while len(q)>=2 and q[0]==q[1]:
                q.popleft()
                q.popleft()

ans=list(q)
ans=''.join(ans)
if flip:
    ans=ans[::-1]
print(ans)