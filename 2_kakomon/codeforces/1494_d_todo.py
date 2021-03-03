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

        # if self.parents[x] > self.parents[y]:
        #     x, y = y, x

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

from heapq import heappop,heappush
n=int(input())
al=[]
for _ in range(n):
    al.append(list(map(int, input().split())))

ansl=[-1]*(2*n)
uf=UnionFind(n*2)
q=[]
for i in range(n):
    for j in range(i+1):
        if i==j:ansl[i]=al[i][i]
        else:
            heappush(q,(al[i][j],i,j))

gl=[]
# print(q)
roots=list(range(0,n*2))
node_i=n
cmax=0
while q:
    a,i,j=heappop(q)
    if uf.same(j,i):continue
    if cmax==a:
        node_i-=1
    rooti=roots[uf.find(i)]
    rootj=roots[uf.find(j)] 
    if rooti+1!=node_i+1: gl.append((rooti+1,node_i+1))
    if rootj+1!=node_i+1: gl.append((rootj+1,node_i+1))
    uf.union(rooti,node_i)
    uf.union(rootj,node_i)
    ansl[node_i]=a
    uf.union(j,node_i)
    uf.union(i,node_i)
    roots[uf.find(j)]=node_i
    roots[uf.find(i)]=node_i
    # roots[uf.find(rootj)]=node_i
    # roots[uf.find(rooti)]=node_i
    # roots[uf.find(node_i)]=node_i
    # print('--',i,j,uf.find(i),uf.find(j),uf.find(node_i))
    node_i+=1
    cmax=max(cmax,a)


print(len(gl)+1)
print(*ansl[:node_i])
print(len(gl)+1)
for u,v in gl:print(u,v)