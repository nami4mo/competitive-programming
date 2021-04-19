n=int(input())
gl=[[] for _ in range(n)]
gll=[]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
    gll.append((a,b))

dists=[-1]*n
from collections import deque
q=deque()
q.append(0)
dists[0]=0

while q:
    poped=q.popleft()
    for neib in gl[poped]:
        if dists[neib]!=-1:continue
        q.append(neib)
        dists[neib]=dists[poped]+1

val=[0]*n
# minus=[0]*n
csum=0
for _ in range(int(input())):
    t,e,x=map(int, input().split())
    a,b=gll[e-1]
    if dists[a]>dists[b]:
        a,b=b,a
        if t==2:t=1
        else:t=2
    if t==1:
        csum+=x
        val[b]-=x
    else:
        val[b]+=x

q=deque()
q.append(0)
dists=[-1]*n
dists[0]=0
while q:
    poped=q.popleft()
    for neib in gl[poped]:
        if dists[neib]!=-1:continue
        q.append(neib)
        dists[neib]=dists[poped]+1
        val[neib]+=val[poped]

for v in val:
    print(v+csum)