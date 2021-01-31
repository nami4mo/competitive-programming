from heapq import heappop, heappush

n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

q=[0]
ansl=[]
visited=[False]*n
visited[0]=True
while q:
    poped=heappop(q)
    ansl.append(poped)
    for neib in gl[poped]:
        if visited[neib]:continue
        heappush(q,neib)
        visited[neib]=True

ansl=[a+1 for a in ansl]
print(*ansl)