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
        return x

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


n,m = map(int, input().split())
costs = []
for i in range(n):
    c = int(input())
    costs.append((c,i,-1))

for _ in range(m):
    a,b,r = map(int, input().split())
    costs.append((r,a-1,b-1))

costs.sort(key=lambda x: x[0])
builts = [False]*n

uf = UnionFind(n)
ans = 0
for cost, a, b in costs:
    if b == -1:
        pare = uf.find(a)
        if not builts[pare]:
            builts[pare] = True
            ans += cost
    else:
        if uf.same(a,b):continue
        else:
            pare_a = uf.find(a)
            pare_b = uf.find(b)
            if builts[pare_a] and builts[pare_b]:continue
            if builts[pare_a] or builts[pare_b]:
                pare = uf.union(a,b)
                builts[pare] = True
                ans += cost
            else:
                pare = uf.union(a,b)
                ans += cost

print(ans)