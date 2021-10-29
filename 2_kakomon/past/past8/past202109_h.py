from collections import deque

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
    if moved_a == moved_b:
        return moved_a, b_up
    
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

def main():
    n,x=map(int, input().split())
    gl=[[] for _ in range(n)]
    gl2=[[] for _ in range(n)]

    for _ in range(n-1):
        a,b,c=map(int, input().split())
        a-=1
        b-=1
        gl[a].append((b,c))
        gl[b].append((a,c))
        gl2[a].append(b)
        gl2[b].append(a)
    dists=[-1]*n
    from collections import deque
    q=deque([0])
    dists[0]=0
    while q:
        poped=q.popleft()
        for neib,d in gl[poped]:
            if dists[neib]!=-1:continue
            dists[neib]=dists[poped]+d
            q.append(neib)

    dist_pares=make_dist_pares(n,gl2,0)
    db=make_doubling(n,dist_pares)
    for i in range(n):
        for j in range(i+1,n):
            lca,_=calc_lca_dist(n,db,dist_pares,i,j)
            # print(i+1,j+1,lca+1)
            d=-1
            if lca==i or lca==j: d=abs(dists[j]-dists[i])
            else:d=dists[i]+dists[j]-2*dists[lca]
            if d==x:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    main()