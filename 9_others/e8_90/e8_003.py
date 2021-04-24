from collections import deque
def get_last(start,gl):
    q=deque()
    q.append(start)
    vis=[-1]*n
    vis[start]=0
    last=start
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if vis[neib]!=-1:continue
            q.append(neib)
            vis[neib]=vis[poped]+1
        last=poped
    return last,vis

n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

u,_=get_last(0,gl)
v,vis=get_last(u,gl)
print(vis[v]+1)