n=int(input())
# sl=[]
el=[]
for i in range(n):
    a,b=map(int, input().split())
    el.append((a,1))
    el.append((a+b,-1))
el.sort(key=lambda x:x[0])

from collections import deque
q=deque(el)

t=0
cval=0
ans=[0]*(n+1)
while q:
    ct=q[0][0]
    while q and q[0][0]==ct:
        _, val=q.popleft()
        cval+=val
    # print(ct,cval)
    if q:
        dist=q[0][0]-ct
        ans[cval]+=dist
print(*ans[1:])