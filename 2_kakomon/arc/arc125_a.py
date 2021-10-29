n,m=map(int, input().split())
sl=list(map(int, input().split()))
tl=list(map(int, input().split()))

from collections import deque
q=deque(tl)
ans=0
while q and q[0]==sl[0]:
    q.popleft()
    ans+=1

if not q:
    print(ans)
    exit()

d=10**9
for i in range(1,n):
    if sl[0]!=sl[i]:
        d=i
        break
for i in range(1,n):
    if sl[0]!=sl[-i]:
        d=min(d,i)
        break
if d==10**9:
    print(-1)
    exit()

ans+=d
tl=list(q)
for i in range(len(tl)-1):
    if tl[i+1]!=tl[i]:ans+=1
ans+=len(tl)
print(ans)