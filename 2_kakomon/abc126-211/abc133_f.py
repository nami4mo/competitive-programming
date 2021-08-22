# 9 5
# 1 2 1 10
# 1 3 1 10
# 2 4 2 10
# 2 5 3 10
# 3 6 2 10
# 3 7 3 10
# 4 8 1 10
# 4 9 3 10
# 1 30 6 8
# 2 30 4 5
# 1 30 1 4
# 3 30 3 9
# 1 30 2 5

# LCA

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,Q=map(int, input().split())
g=[[] for _ in range(n)]
for _ in range(n-1):
    x,y,c,d = map(int, input().split())
    x-=1
    y-=1
    c-=1
    g[x].append((y,c,d))
    g[y].append((x,c,d))

from collections import deque
q = deque([0])
dist_pares = [(-1,-1,-1)]*n
dist_pares[0] = (0,0,0)
while q:
    poped = q.popleft()
    dist = dist_pares[poped][0]
    pare_node = dist_pares[poped][1]
    dist,depth,pare_node=dist_pares[poped]
    for neib,c,d in g[poped]:
        if neib != pare_node:
            q.append(neib)
            dist_pares[neib] = (dist+d, depth+1, poped)

# print(dist_pares)

from math import log2
logn = int(log2(n))+1
db = [ [0]*n for _ in range(logn) ]
for ni in range(n): 
    db[0][ni] = dist_pares[ni][2]
for ki in range(logn-1):
    for ni in range(n):
        db[ki+1][ni] = db[ki][db[ki][ni]]

node_cl=[set() for _ in range(n)]
ql=[]
for _ in range(Q):
    x,y,a,b=map(int, input().split())
    x-=1 # color
    a-=1
    b-=1
    node_cl[a].add(x)
    node_cl[b].add(x)
#     ql.append((x,y,u,v))

# for q_ in range(Q):
#     x,y,a,b=ql[q_]
    dist_a = dist_pares[a][1]
    dist_b = dist_pares[b][1]
    if dist_a > dist_b:
        dist_a,dist_b = dist_b,dist_a
        a,b = b,a

    moved_a = a
    moved_b = b
    b_up = dist_b-dist_a 
    for i in range(logn):
        if b_up&(1<<i) > 0:
            moved_b = db[i][moved_b]

    for i in range(logn-1,-1,-1):
        if db[i][moved_a] != db[i][moved_b]:
            moved_a = db[i][moved_a]
            moved_b = db[i][moved_b]
    if moved_a==moved_b: lca=moved_b
    else: lca=db[0][moved_b]
    node_cl[lca].add(x)
    ql.append((x,y,a,b,lca))

# print(ql)

node_dl=[{} for _ in range(n)]
for save_c in list(node_cl[0]):
    node_dl[0][save_c] = (0,0)

curr_cl=[(0,0)]*(n-1)
def dfs(node,pare,edge_cd=None):
    # print(node,curr_cl)
    for neib,c,d in g[node]:
        if neib==pare: continue
        clc=curr_cl[c]
        curr_cl[c]=(clc[0]+1,clc[1]+d)
        for save_c in list(node_cl[neib]):
            node_dl[neib][save_c] = curr_cl[save_c]
        dfs(neib,node,(c,d))
    if edge_cd:
        clc=curr_cl[edge_cd[0]]
        curr_cl[edge_cd[0]]=(clc[0]-1,clc[1]-edge_cd[1])

dfs(0,-1)

# print(node_dl)
# print(node_cl)

for x,y,a,b,lca in ql:
    # print(a+1,b+1,lca+1,'---')
    dist_a = dist_pares[a][0]
    dist_b = dist_pares[b][0]

    dlca=dist_pares[lca][0]
    raw_dist=dist_a+dist_b-dlca*2

    col_n = node_dl[a][x][0]+node_dl[b][x][0]-node_dl[lca][x][0]*2
    col_d = node_dl[a][x][1]+node_dl[b][x][1]-node_dl[lca][x][1]*2
    new_d = col_n*y
    diff = new_d-col_d
    ans=raw_dist+diff

    print(ans)