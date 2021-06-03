n,a=map(int, input().split())
a-=1
s=input()

from collections import deque
lq=deque([-1])
rq=deque()
for i in range(n):
    if s[i]=='#':
        if i<a:lq.append(i)
        else:rq.append(i)
rq.append(n)

need=len(lq)+len(rq)-2
ans=0
cnt=0
pos=a
di=1
while cnt<need:
    if di==1:
        to=rq[0]
        if rq[0]!=n:
            rq.popleft()
            cnt+=1
        ans+=(to-pos)
        pos=to
    else:
        to=lq[-1]
        if lq[-1]!=-1:
            lq.pop()
            cnt+=1
        ans+=(pos-to)
        pos=to
    di*=-1
    # print(pos)

print(ans)