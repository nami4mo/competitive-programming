n=int(input())
abl=[]
gl=[[] for _ in range(n)]

from collections import deque
q=deque()
vis=[False]*n
al=[]

for i in range(n):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(i)
    gl[b].append(i)
    if a==i or b==i:
        start=i
        al.append(i)
        vis[i]=True
        q.append(i)

if not q:
    print(-1)
    exit()

# print(gl)

while q:
    poped=q.popleft()
    for neib in gl[poped]:
        if vis[neib]:continue
        al.append(neib)
        q.append(neib)
        vis[neib]=True

if len(al)==n:
    for a in al[::-1]:
        print(a+1)
else:
    print(-1)