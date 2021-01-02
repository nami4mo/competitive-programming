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


n,m = map(int, input().split())
sl = []
notwall = 0
for _ in range(n):
    s = list(input())
    notwall += s.count('.')
    sl.append(s)

ans = 0
for i in range(n):
    for j in range(m):
        if sl[i][j] == '.': continue
        uf = UnionFind(n*m)
        for h in range(n):
            for w in range(m):
                if sl[h][w] == '#' and (i,j) != (h,w): continue
                for dh,dw in [[-1,0],[1,0],[0,-1],[0,1]]:
                    if 0 <= h+dh < n and 0 <= w+dw < m and sl[h+dh][w+dw] == '.':
                        uf.union(h*m+w, (h+dh)*m+(w+dw) )
        # print(uf.size(i*m+j))
        if uf.size(i*m+j) == notwall+1:
            ans += 1

print(ans)