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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    # n: 0-ind, m: 1-ind
    n,m = map(int, input().split())
    ml = [ [] for _ in range(m+1)]
    
    # 0~n-1: people (-1), n~n+m-1: lang (+n-1)
    uf = UnionFind(n+m)

    for i in range(n):
        ll = list(map(int, input().split()))[1:]
        for l in ll:
            uf.union(i,l+n-1)
    
    for i in range(n):
        if not uf.same(0,i):
            print('NO')
            break
    else:
        print('YES')
        


if __name__ == "__main__":
    main()