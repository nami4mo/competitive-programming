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


n,m,k = map(int, input().split())
uf = UnionFind(n+1)
direct_cnts = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    uf.union(a,b)
    direct_cnts[a] += 1
    direct_cnts[b] += 1


block = [[] for _ in range(n+1)]
for _ in range(k):
    c,d = map(int, input().split())
    block[c].append(d)
    block[d].append(c)


ansl = []
for i in range(1,n+1):
    cnt = uf.size(i)-1
    cnt -= direct_cnts[i]
    for b in block[i]:
        if uf.same(i,b): cnt -= 1
    ansl.append(cnt)

print(*ansl)