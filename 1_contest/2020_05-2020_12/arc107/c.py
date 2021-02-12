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



n,k = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(n)]
uf_row = UnionFind(n)
uf_col = UnionFind(n)


for i in range(n):
    for j in range(i,n):
        for m in range(n):
            if al[i][m] + al[j][m] > k:
                break
        else:
            uf_row.union(i,j)

for i in range(n):
    for j in range(i,n):
        for m in range(n):
            if al[m][i] + al[m][j] > k:
                break
        else:
            uf_col.union(i,j)

vsr = uf_row.get_all_members()
vsc = uf_col.get_all_members()

MOD = 998244353
kaijo = [1]
for i in range(1,51):
    v = kaijo[-1]*i
    v%=MOD
    kaijo.append(v)

# print(kaijo)

ans = 1
for vs in vsr:
    ans *= kaijo[len(vs)]
    ans %= MOD

for vs in vsc:
    ans *= kaijo[len(vs)]
    ans %= MOD

print(ans)