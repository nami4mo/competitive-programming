from collections import deque

n=int(input())
gl=[[] for i in range(n)]
el=[]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
    el.append((a,b))

dists=[-1]*n
dists[0]=0
q=deque([0])
while q:
    poped=q.popleft()
    for neib in gl[poped]:
        if dists[neib]!=-1:continue
        dists[neib]=dists[poped]+1
        q.append(neib)

# print(dists)
allsum=0
vl=[0]*n
q=int(input())
for i in range(q):
    t,e,x=map(int, input().split())
    a,b=el[e-1]
    if t==1:
        if dists[a]<dists[b]:
            vl[b]-=x
            allsum+=x
        else:
            vl[a]+=x
    else:
        if dists[b]<dists[a]:
            vl[a]-=x
            allsum+=x
        else:
            vl[b]+=x

dists=[-1]*n
dists[0]=0
q=deque([0])
while q:
    poped=q.popleft()
    for neib in gl[poped]:
        if dists[neib]!=-1:continue
        dists[neib]=dists[poped]+1
        vl[neib]+=vl[poped]
        q.append(neib)

for a in vl:
    print(a+allsum)