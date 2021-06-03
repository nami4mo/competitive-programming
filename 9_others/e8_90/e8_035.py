from collections import deque
def make_dfs_order(n,gl,root=0):
    res=[]
    vis=[False]*n
    q=deque()
    q.append(root)
    vis[root]=True
    while q:
        poped=q.popleft()
        res.append(poped)
        for neib in gl[poped]:
            if vis[neib]:continue
            vis[neib]=True
            q.appendleft(neib)
    return res


# --- calc (dist-from-root, parent) of all the nodes ---
def make_dist_pares(n,gl,root=0):
    q = deque([root])
    dist_pares = [(-1,-1)]*n
    dist_pares[root] = (0,root)
    while q:
        poped = q.popleft()
        dist = dist_pares[poped][0]
        pare_node = dist_pares[poped][1]
        for next_node in gl[poped]:
            if next_node != pare_node:
                q.append(next_node)
                dist_pares[next_node] = (dist+1, poped)
    return dist_pares


# --- doubling (for calulating the parent) ---
from math import log2
def make_doubling(n,dist_pares):
    logn = int(log2(n))+1
    db = [ [0]*n for _ in range(logn) ]
    for ni in range(n): 
        db[0][ni] = dist_pares[ni][1]
    for ki in range(logn-1):
        for ni in range(n):
            db[ki+1][ni] = db[ki][db[ki][ni]]
    return db

# --- doubling: find the lca and dist of/between the two nodes(a,b) ---
def calc_lca_dist(n, db, dist_pares, a, b):
    logn = int(log2(n))+1

    dist_a = dist_pares[a][0]
    dist_b = dist_pares[b][0]
    if dist_a > dist_b:
        dist_a,dist_b = dist_b,dist_a
        a,b = b,a

    # --- for depth-a == depth-b ---
    moved_a = a
    moved_b = b
    b_up = dist_b-dist_a 
    for i in range(logn):
        if b_up&(1<<i) > 0:
            moved_b = db[i][moved_b]
    
    # --- search LCA ---
    dist = b_up
    for i in range(logn-1,-1,-1):
        if db[i][moved_a] != db[i][moved_b]:
            moved_a = db[i][moved_a]
            moved_b = db[i][moved_b]
            # dist += 2*pow(2,i)
            dist += 2*(1<<i)
    if moved_a != moved_b: dist += 2
    lca = db[0][moved_b]
    return lca,dist


n=int(input())
gl=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)

dfs_order=make_dfs_order(n,gl,0)
# print(dfs_order)
i2o={}
for i in range(n):
    i2o[dfs_order[i]]=i


dist_pares=make_dist_pares(n,gl,0)
db=make_doubling(n,dist_pares)

ansl=[]
for _ in range(int(input())):
    kl=list(map(int, input().split()))[1:]
    dl=[i2o[k-1] for k in kl]
    dl.sort()
    dl.append(dl[0])
    val=0
    for i in range(len(dl)-1):
        a,b=dfs_order[dl[i]],dfs_order[dl[i+1]]
        _,dist=calc_lca_dist(n,db,dist_pares,a,b)
        # print('--')
        # print(a,b)
        # print(dist)
        val+=dist
    ansl.append(val//2)

for a in ansl:print(a)