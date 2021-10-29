n,m=map(int, input().split())
from collections import deque

al=[]
tops1=[-1]*(n+1)
tops2=[-1]*(n+1)
cq=deque()

for i in range(m):
    k=int(input())
    row=list(map(int, input().split()))
    al.append(deque(row))
    a=row[0]
    if tops1[a]==-1:
        tops1[a]=i
    elif tops1[a]!=-1:
        tops2[a]=i
        cq.append(a)

cnt=0
while cq:
    cnt+=1
    col=cq.popleft()
    p1=tops1[col]
    p2=tops2[col]
    # print(col,p1,p2)
    for p in [p1,p2]:
        if al[p]:
            al[p].popleft()
            if not al[p]:continue
            cc=al[p][0]
            if tops1[cc]==-1:
                tops1[cc]=p
            else:
                tops2[cc]=p
                cq.append(cc)
if cnt==n:
    print('Yes')
else:print('No')