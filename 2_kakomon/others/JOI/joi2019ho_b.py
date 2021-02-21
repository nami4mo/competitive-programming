n,m=map(int, input().split())
vsl=[]
for _ in range(n):
    s,v=map(int, input().split())
    vsl.append((v,s))

vsl.sort(key=lambda x:(-x[0],-x[1]))
cl=[int(input()) for _ in range(m)]
cl.sort(reverse=True)

from collections import deque
vsq=deque(vsl)
cq=deque(cl)

ans=0
while vsq and cq:
    v,s=vsq.popleft()
    if cq[0]>=s:
        ans+=1
        cq.popleft()

print(ans)