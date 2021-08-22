from typing import DefaultDict


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

n = int(input())
uf = UnionFind(2*(10**5)+2)

for _ in range(n):
    x,y = map(int, input().split())
    uf.union(x,y+10**5)

root_x_cnts = DefaultDict(int)
root_y_cnts = DefaultDict(int)
for i in range(1,10**5+1):
    root_x_cnts[uf.find(i)]+=1
    root_y_cnts[uf.find(i+10**5)]+=1

ans = 0
for k in root_x_cnts.keys():
    ans += root_x_cnts[k]*root_y_cnts[k]

# print(root_x_cnts)
# print(root_y_cnts)
print(ans-n)