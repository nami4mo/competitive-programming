from collections import deque
from math import log2

n = int(input())
g = [ [] for _ in range(n+1) ]
root = -1
for i in range(n):
    syain = i+1
    # x,y = map(int, input().split())
    # x-=1
    # y-=1
    # g[x].append(y)
    # g[y].append(x)
    p = int(input())
    if p == -1: root = syain
    else:
        g[p].append(syain)


q = deque([root])
dist_pares = [(-1,-1)]*(n+1)
dist_pares[root] = (0,root)
while q:
    poped = q.popleft()
    dist = dist_pares[poped][0]
    pare_node = dist_pares[poped][1]
    for next_node in g[poped]:
        if next_node != pare_node:
            q.append(next_node)
            dist_pares[next_node] = (dist+1, poped)
# print(dist_pares)

# --- doubling (for calulating the parent) ---
logn = int(log2(n))+1
db = [ [0]*(n+1) for _ in range(logn) ]
for ni in range(n+1): 
    db[0][ni] = dist_pares[ni][1]
for ki in range(logn-1):
    for ni in range(n+1):
        db[ki+1][ni] = db[ki][db[ki][ni]]

# print(dist_pares)
# print(db)

q = int(input())
for _ in range(q):
    a,b = map(int, input().split())
    adist = dist_pares[a][0]
    bdist = dist_pares[b][0]
    if adist <= bdist:
        print('No')
    else:
        dist = adist-bdist
        now = a
        for i in range(logn):
            if dist&(1<<i) > 0:
                now = db[i][now]
        if now == b:
            print('Yes')
        else:
            print('No')