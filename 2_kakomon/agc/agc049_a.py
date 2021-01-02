from collections import deque
def dfs(start, gl, n):
    visited=[False]*n
    visited[start]=True
    q=deque([start])
    vcnt=1
    while q:
        poped=q.popleft()
        for neib in gl[poped]:
            if visited[neib]:continue
            visited[neib]=True
            q.appendleft(neib)
            vcnt+=1
    return vcnt

n=int(input())
gl=[[] for _ in range(n)]
glr=[[] for _ in range(n)]
for i in range(n):
    row=list(input())
    for j in range(n):
        if row[j]=='1':
            gl[i].append(j)
            glr[j].append(i)

ans=0
for start in range(n):
    cnt=dfs(start,glr,n)
    ans+=1/cnt
print(ans)
