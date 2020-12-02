from collections import deque
n=int(input())
gl=[[]for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

al=list(map(int, input().split()))
al.sort(reverse=True)
qa=deque(al)

visited=[-1]*n
q=deque()
q.append(0)
visited[0]=qa.popleft()
while q:
    poped=q.popleft()
    for v in gl[poped]:
        if visited[v]!=-1:continue
        visited[v]=qa.popleft()
        q.append(v)

print(sum(al[1:]))
print(*visited)