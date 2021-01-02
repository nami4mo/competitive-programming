from math import sqrt
from itertools import product

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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



def kruskal(es,n):
    uf = UnionFind(n)
    es.sort(key=lambda v: v[2])
    ans = 0
    for u,v,d in es:
        if uf.same(u,v): continue
        uf.union(u,v)
        ans += d
    return ans


n,m = map(int, input().split())
xycl = []
for _ in range(n):
    x,y,c = map(int, input().split())
    xycl.append((x,y,c))

mxycl = []
for _ in range(m):
    x,y,c = map(int, input().split())
    mxycl.append((x,y,c))

es = []
for i in range(n):
    for j in range(i+1,n):
        xi,yi,ci = xycl[i]
        xj,yj,cj = xycl[j]
        d = sqrt((xi-xj)**2+(yi-yj)**2)
        if ci != cj: d*=10
        es.append((i,j,d))

# print(es)

ans = 10**18
ite = list(product(range(2),repeat=m))
for pattern in ite:
    added_es = []
    ms = []
    for i, v in enumerate(pattern):
        if v == 0: continue
        ms.append(i)
    for mi in ms:
        xm,ym,cm = mxycl[mi]
        for i in range(n):
            xi,yi,ci = xycl[i]
            d = sqrt((xi-xm)**2+(yi-ym)**2)
            if ci != cm: d*=10
            added_es.append((i,mi+n,d))
        for mmi in ms:
            if mi == mmi: continue
            xi,yi,ci = mxycl[mmi]
            d = sqrt((xi-xm)**2+(yi-ym)**2)
            if ci != cm: d*=10
            added_es.append((mmi+n,mi+n,d))
    # print(added_es)
    c_ans = kruskal(es+added_es, n+m)
    ans = min(ans,c_ans)

print(ans)