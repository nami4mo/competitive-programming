
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

from math import sqrt
def p2p(p1,p2):
    x1,y1,_=p1
    x2,y2,_=p2
    return sqrt((x1-x2)**2+(y1-y2)**2)

def p2c(point,circle):
    px,py,_=point
    cx,cy,cr,_=circle
    d=sqrt((px-cx)**2+(py-cy)**2)
    return abs(d-cr)

def c2c(c1,c2):
    x1,y1,r1,_=c1
    x2,y2,r2,_=c2
    d=sqrt((x1-x2)**2+(y1-y2)**2)
    if d>r1+r2:
        return d-(r1+r2)
    if d<abs(r1-r2):
        return abs(r1-r2)-d
    return 0

n,m=map(int, input().split())
pl=[]
cl=[]
for i in range(n):
    x,y=map(int, input().split())
    pl.append((x,y,i))
for i in range(m):
    x,y,r=map(int, input().split())
    cl.append((x,y,r,i+n))

gl=[]
for i in range(n):
    for j in range(i+1,n):
        d=p2p(pl[i],pl[j])
        gl.append((i,j,d))
    
for i in range(n):
    for j in range(m):
        d=p2c(pl[i],cl[j])
        gl.append((i,j+n,d))

for i in range(m):
    for j in range(i+1,m):
        d=c2c(cl[i],cl[j])
        gl.append((i+n,j+n,d))

gl.sort(key=lambda v: v[2])

# print(gl)
ans=10**18
from itertools import product
ite = list(product(range(2),repeat=m))
for pattern in ite:
    usem=[False]*m
    for i, v in enumerate(pattern):
        if v==1:usem[i]=True
    
    uf = UnionFind(n+m)
    cost = 0
    for u,v,d in gl:
        if uf.same(u,v): continue
        if u>=n and not usem[u-n]:continue
        if v>=n and not usem[v-n]:continue
        uf.union(u,v)
        cost += d
    ans=min(ans,cost)
    # for i in range(n-1):
    #     if not uf.same(i,i+1):
    #         print(pattern)
    #         break
    # else:
        # ans=min(ans,cost)
print(ans)