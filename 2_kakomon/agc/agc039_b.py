from collections import deque
n=int(input())
gl=[[] for _ in range(n)]
for i in range(n):
    row = list(input())
    for j in range(n):
        if row[j] == '1':
            gl[i].append(j)


ans = -1
for start in range(n):
    dists=[-1]*n
    dists[start]=0
    q = deque([start])
    ok_flag = True
    while q:
        node = q.popleft()
        for neib in gl[node]:
            if dists[neib]!=-1 and abs(dists[neib]-dists[node])!=1:
                ok_flag = False
                break
            if dists[neib] == -1:
                q.append(neib)
            dists[neib] = dists[node]+1
    if ok_flag:
        ans = max(ans, max(dists))

print(ans)