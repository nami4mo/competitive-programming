import sys
sys.setrecursionlimit(10**6)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        ## if parents[i]>=0 => parents[i] is parent of i
        ## if parents[i]<0 => i is root and (-1)*parents[i] shows the group size.

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        # if size[x] < size[y]: => swap (x group: larger, y group: smaller)
        # to merge the smaller group(y) into the larger(x)
        if self.parents[x] > self.parents[y]: 
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    # too slow
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def get_all_members(self):
        pare_d = {}
        for i in range(self.n):
            parent = self.find(i)
            pare_d.setdefault(parent,[])
            pare_d[parent].append(i)
        return list(pare_d.values())

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def dfs1(node, gl, order, cnt, n, vis, prevs):
    for neib in gl[node]:
        if vis[neib]:continue
        vis[neib]=True
        order.append(neib)
        prevs[neib]=node
        dfs1(neib, gl, order, cnt+1, n, vis, prevs)
        

def dfs2(ind, gl, order, prevs, cs, n, ans, gl2):
    if ind==n:
        check=True
        for cn in order:
            for neib in gl2[cn]:
                if cs[cn]==cs[neib]:
                    check=False
                    break
            if not check:break
        if check: ans[0]+=1
        return 

    node_i=order[ind]
    for c in range(3):
        if prevs[node_i]!=-1 and cs[prevs[node_i]]==c: continue
        cs[node_i]=c
        dfs2(ind+1, gl, order, prevs, cs, n, ans, gl2)
        cs[node_i]=-1


def solve(nodes,gl,nn,gl2):
    n=len(nodes)
    start=nodes[0]
    order=[start]
    prevs=[-1]*nn
    vis=[False]*nn
    vis[start]=True
    dfs1(start, gl, order, 0, n, vis, prevs)

    cs=[-1]*nn
    cs[start]=0
    ans=[0]
    dfs2(1, gl, order, prevs, cs, n, ans, gl2)
    return ans[0]*3



n,m=map(int, input().split())
uf=UnionFind(n)
gl=[[] for _ in range(n)]
gl2=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int, input().split())
    a-=1
    b-=1
    gl[a].append(b)
    gl[b].append(a)
    uf.union(a,b)
    gl2[min(a,b)].append(max(a,b))

nodes=uf.get_all_members()
pat=1
for gr in nodes:
    pat*=solve(gr,gl,n,gl2)

print(pat)