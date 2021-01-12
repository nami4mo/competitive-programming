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

MAX=400001
n=int(input())
uf=UnionFind(MAX)
cnts=[0]*MAX
abl=[]
for _ in range(n):
    a,b=map(int, input().split())
    cnts[a]+=1
    cnts[b]+=1
    uf.union(a,b)
    abl.append((a,b))

group_cnt=uf.group_count()
edge_cnts={}
for a,b in abl:
    root=uf.find(a)
    edge_cnts.setdefault(root,0)
    edge_cnts[root]+=1

ans=0
all_groups=uf.get_all_members()
for group in all_groups:
    if cnts[group[0]]==0:continue
    member_cnt=len(group)
    if edge_cnts[uf.find(group[0])] == member_cnt-1:
        ans+=(member_cnt-1)
    else:
        ans+=member_cnt
print(ans)